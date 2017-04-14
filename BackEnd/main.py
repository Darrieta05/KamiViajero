# -*- coding=UTF-8 -*-

import bcrypt
import os
from flask import Flask, json, Response, request, session
from flask_pymongo import PyMongo
from functools import wraps
from Datos import viaje_datos as datos_viaje, transporte_datos as datos_transporte, algoritmo_dijkstra
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.secret_key= os.urandom(24)
CORS(app)


#conexión a la base de datos
app.config['MONGO_DBNAME'] = 'tribot'
app.config['MONGO_URI'] = 'mongodb://tribot:tribot@ds157390.mlab.com:57390/tribot'

mongo = PyMongo(app)

#-------inicio bloque de manejo de errores-------
@app.errorhandler(405)
def handle_bad_server(e):
    return 'Intenta cambiando de metodo o revisa bien los parametros'

@app.errorhandler(500)
def handle_bad_server(e):
    return 'Servidor incorrecto'

@app.errorhandler(404)
def handle_bad_request(e):
    return 'No se encuentra'

@app.errorhandler(400)
def handle_bad_request(e):
    return 'Solicitud incorrecta'
#-------fin bloque de manejo de errores----------

#guarda la consulta más reciente de una ruta
info_temporal = {}

@app.route('/registrar',methods=['POST','GET'])
def registrar():
    users = mongo.db.users

    if request.method == 'POST':
        nombre = request.json["nombre"]
        apellido = request.json["apellido"]
        usuario = request.json["usuario"]
        password = request.json["password"]

        users = mongo.db.users

        usuario_existente = users.find_one({"usuario": usuario})

        if usuario_existente is None:
            hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users.insert({'nombre':nombre,'apellido':apellido,'usuario':usuario,'password':hashpass})

            session['usuario'] = usuario

            json_registrar = ({'usuario': session['usuario']})
            resultado = json.dumps(json_registrar)
            respuesta = Response(resultado, status=200, mimetype='application/json')
            respuesta.headers['Access-Control-Allow-Origin'] = "*"
            return respuesta

        json_registrar = ({'error': 'El usuario ya existe!'})
        resultado = json.dumps(json_registrar)
        respuesta = Response(resultado, status=200, mimetype='application/json')
        respuesta.headers['Access-Control-Allow-Origin'] = "*"
        return respuesta


    return 'Redireccionar a registro'

#este metodo se utiliza como wrapper para las rutas que necesitan authentication
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'usuario' in session:
            return test(*args, **kwargs)
        else:
            return 'Es necesario iniciar sesion'
    return wrap

@app.route('/login',methods=['POST'])
def login():
    users = mongo.db.users
    usuario = request.json["usuario"]
    password = request.json["password"]

    login_user = users.find_one({'usuario':usuario})

    if login_user:
        if bcrypt.hashpw(password.encode('utf-8'), login_user['password']) == login_user['password']:
            session['usuario'] = usuario

            json_login = ({'usuario': session['usuario']})
            resultado = json.dumps(json_login)
            respuesta = Response(resultado, status=200, mimetype='application/json')
            respuesta.headers['Access-Control-Allow-Origin'] = "*"

            return respuesta

    json_login = ({'error': 'Usuario y/o contraseña incorrectos'})
    resultado = json.dumps(json_login)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    respuesta.headers['Access-Control-Allow-Origin'] = "*"
    return respuesta

@app.route('/logout')
def logout():
    session.pop('usuario',None)

    json_logout = ({'logout': 'Has cerrado sesion'})
    resultado = json.dumps(json_logout)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    respuesta.headers['Access-Control-Allow-Origin'] = "*"
    return respuesta


@app.route('/destinos',methods=['GET'])
# @login_required
def destinos():

    resultado = json.dumps(datos_transporte.Info_Rutas.destinos)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    respuesta.headers['Access-Control-Allow-Origin'] = "*"
    return respuesta

@app.route('/transporte_disponible',methods=['POST'])
# @login_required
def transporte_disponible():
    nodosVisitados = []
    distancia = {}
    nodoAnterior = {}
    ruta = []

    punto_inicio = request.json["inicio"]
    punto_destino = request.json["destino"]


    #guarda en una variable el resultado del algoritmo
    ruta_mas_corta = algoritmo_dijkstra.dijkstra(algoritmo_dijkstra.grafo, punto_inicio, punto_destino, nodosVisitados, distancia, nodoAnterior)

    #se inicializa la lista que guardará el nombre de los puntos que recorre el algoritmo para llegar al destino

    transporte = datos_transporte.Info_Rutas()
    transporte_disponible = transporte.habilitaTransporte(punto_inicio,punto_destino)

    #por cada punto guardado en el camino de la ruta mas corta
    #busca el id de la ruta en el json "destinos" para encontrar su nombre correspondiente y lo agrega a la lista
    for destino in ruta_mas_corta['Ruta']:
        ruta.append(datos_transporte.Info_Rutas.destinos[destino])

    #se le da formato el json que se retorna
    temporal=({'Distancia':ruta_mas_corta['Distancia'],'Ruta': (ruta),'Transporte':transporte_disponible})
    info_temporal[0] = temporal

    json_ruta = ({'transporte': transporte_disponible})
    resultado = json.dumps(json_ruta)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    respuesta.headers['Access-Control-Allow-Origin'] = "*"

    return respuesta

@app.route('/tarifa', methods=['POST'])
# @login_required
def tarifa():

    try:
        transporte_seleccionado = request.json['transporte']
        punto_inicio = request.json["inicio"]
        punto_destino = request.json["destino"]
        distancia = float(info_temporal[0]['Distancia'])


        if transporte_seleccionado == "Taxi":

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionTaxi(distancia)

            tarifa = datos_viaje.Datos_Tarifas()
            tarifa_total = tarifa.TarifaTaxi(distancia)

            ejecutar_db = mongo.db.transporte_taxis
            taxis = []

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionBus(distancia)

            for taxi in ejecutar_db.find({'compania': "Taxis TriBot"}):
                taxis.append(
                    {"compania": taxi["compania"], "conductor": taxi["conductor"], "id_conductor": taxi["id_conductor"],
                     "placa": taxi["placa"], "contacto": taxi["contacto"],"precio_kilometro": taxi["precio_kilometro"],"tarifa_base": taxi["tarifa_base"]})

            json_ruta = (
                {'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Taxi",
                 'Duracion': duracion_estimada, 'Tarifa':tarifa_total, 'Taxis_disponibles': taxis})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Bus":

            pasaje = datos_viaje.Datos_Tarifas()
            pasaje_total = pasaje.TarifaBus(punto_inicio,punto_destino)

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionBus(distancia)

            ejecutar_db = mongo.db.transporte_buses
            buses = []
            for bus in ejecutar_db.find({'ruta': {'inicio': punto_inicio,'destino': punto_destino}}):
                buses.append(
                    {"compania": bus["compania"], "conductor": bus["conductor"], "espacios": bus["espacios"],"horarios": bus["horarios"],"contacto": bus["contacto"] })

            json_ruta = (
            {'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Bus",
             'Duracion': duracion_estimada, 'Pasaje': pasaje_total,'Buses_disponibles':buses})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Tren":

            pasaje = datos_viaje.Datos_Tarifas()
            pasaje_total = pasaje.TarifaTren(punto_inicio,punto_destino)

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionTren(distancia)

            ejecutar_db = mongo.db.transporte_tren
            trenes = []

            for tren in ejecutar_db.find({'ruta': {'inicio': punto_inicio,'destino': punto_destino}}):
                trenes.append(
                    {"compania": tren["compania"], "Horario": tren["Horario"],"contacto": tren["contacto"] })

            json_ruta = (
            {'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Tren",
             'Duracion': duracion_estimada, 'Pasaje': pasaje_total,'Tren_disponible':trenes})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Avion":
            distancia_avion = distancia * 0.40
            distancia_total = int(distancia - distancia_avion)


            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionAvion(distancia_total)

            tarifa = datos_viaje.Datos_Tarifas()
            tarifa_total = tarifa.TarifaAvion(distancia_total)

            ejecutar_db = mongo.db.transporte_avion
            aviones = []

            for avion in ejecutar_db.find({'ruta': {'inicio': punto_inicio, 'destino': punto_destino}}):
                aviones.append(
                    {"compania": avion["compania"], "Pasajeros": avion["Pasajeros"], "Horario": avion["Horario"],
                     "contacto": avion["contacto"]})

            json_ruta = (
                {'Distancia': distancia_total, 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Avion",
                 'Duracion': duracion_estimada, 'Pasaje': tarifa_total, 'Vuelos_disponibles': aviones})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')


    except(KeyError):
        #si no se a ejecutado "/elegir_ruta " devuelva el siguiente msj de error
        resultado = json.dumps({'Error':'Ruta no seleccionada'})
        error = Response(resultado, status=200, mimetype='application/json')
        error.headers['Access-Control-Allow-Origin'] = "*"
        return error
    # 
    # respuesta.headers['Access-Control-Allow-Origin'] = "*"
    return respuesta

@app.route('/ranking', methods=['GET'])
# @login_required
def ranking():
    ranking = []
    ejecutar_db = mongo.db.ranking

    for i in ejecutar_db.find():
        ranking.append({"ranking": i["rutas"]})

    json_ruta = ({'Top_5': ranking})
    resultado = json.dumps(json_ruta)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    respuesta.headers['Access-Control-Allow-Origin'] = "*"

    return respuesta


## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
