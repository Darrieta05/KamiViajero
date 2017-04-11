# -*- coding=UTF-8 -*-

import bcrypt
from flask import Flask, json, Response, request, session,g
from flask_pymongo import PyMongo
from flask_httpauth import HTTPBasicAuth

from Datos import viaje_datos as datos_viaje, transporte_datos as datos_transporte, algoritmo_dijkstra

auth = HTTPBasicAuth()

app = Flask(__name__)
app.secret_key='my_secret_key'


#conexión a la base de datos
app.config['MONGO_DBNAME'] = 'tribot'
app.config['MONGO_URI'] = 'mongodb://tribot:tribot@ds157390.mlab.com:57390/tribot'

mongo = PyMongo(app)

#guarda la consulta más reciente de una ruta
info_temporal = {}

@app.route('/registrar',methods=['POST','GET'])
def registrar():
    users = mongo.db.users

    if request.method == 'POST':
        nombre = request.json["nombre"]
        apellido = request.json["apellido"]
        usuario = request.json["usuario"]
        contrasena = request.json["contrasena"]

        users = mongo.db.users

        usuario_existente = users.find_one({"usuario": usuario})

        if usuario_existente is None:
            hashpass = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
            users.insert({'nombre':nombre,'apellido':apellido,'usuario':usuario,'contrasena':hashpass})
            session['usuario'] = usuario
            return "Te has registrado correctamente " + session['usuario']

        return 'El usuario ya existe!'


    return 'Redireccionar a registro'

@app.route('/login',methods=['POST'])
@auth.verify_password
def login():
    users = mongo.db.users
    usuario = request.json["usuario"]
    contrasena = request.json["contrasena"]

    login_user = users.find_one({'usuario':usuario})

    if login_user:
        if bcrypt.hashpw(contrasena.encode('utf-8'), login_user['contrasena']) == login_user['contrasena']:
            session['usuario'] = usuario
            g.user = usuario
            logged = True
            return logged
           # "Te has logeado como " + session['usuario']
        nolog = False
    return nolog

@app.route('/destinos',methods=['GET'])
@auth.login_required
def destinos():

    resultado = json.dumps(datos_transporte.Info_Rutas.destinos)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    respuesta.headers['Access-Control-Allow-Origin'] = "*"
    return respuesta

@app.route('/transporte_disponible',methods=['POST'])
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

            json_ruta = ({'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Taxi",'Duracion':duracion_estimada,'Tarifa':tarifa_total})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Bus":
            ejecutar_db = mongo.db.transporte_buses
            buses = []

            pasaje = datos_viaje.Datos_Tarifas()
            pasaje_total = pasaje.TarifaBus(punto_inicio,punto_destino)

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionBus(distancia)

            for bus in ejecutar_db.find({'ruta': {'inicio': '8','destino': '24'}}):
                buses.append(
                    {"compania": bus["compania"], "conductor": bus["conductor"], "espacios": bus["espacios"],"horarios": bus["horarios"],"contacto": bus["contacto"] })

            #bus = ejecutar_db.find({'capacidad': 25})



            #print(bus)
            json_ruta = (
            {'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Bus",
             'Duracion': duracion_estimada, 'Pasaje': pasaje_total,'Buses_disponibles':buses})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Tren":

            ejecutar_db = mongo.db.transporte_tren
            tren = []

            pasaje = datos_viaje.Datos_Tarifas()
            pasaje_total = pasaje.TarifaTren(punto_inicio,punto_destino)

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionTren(distancia)

            for bus in ejecutar_db.find({'ruta': {'inicio': "1",'destino': "2"}}):
                tren.append(
                    {"compania": bus["compania"], "conductor": bus["conductor"], "capacidad": bus["capacidad"],"horarios": bus["horarios"],"contacto": bus["contacto"] })




            #print(bus)
            json_ruta = (
            {'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Bus",
             'Duracion': duracion_estimada, 'Pasaje': pasaje_total,'Buses_disponibles':tren})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Avion":
            distancia_avion = distancia * 0.40
            distancia_total = int(distancia - distancia_avion)


            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionAvion(distancia_total)

            tarifa = datos_viaje.Datos_Tarifas()
            tarifa_total = tarifa.TarifaAvion(distancia_total)

            json_ruta = (
            {'Distancia': distancia_total, 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Avion",
             'Duracion': duracion_estimada, 'Tarifa': tarifa_total})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

    except(KeyError):
        #si no se a ejecutado "/elegir_ruta " devuelva el siguiente msj de error
        resultado = json.dumps({'Error':'Ruta no seleccionada'})
        error = Response(resultado, status=200, mimetype='application/json')
        error.headers['Access-Control-Allow-Origin'] = "*"
        return error

    respuesta.headers['Access-Control-Allow-Origin'] = "*"
    return respuesta



## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
