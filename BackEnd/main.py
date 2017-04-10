from flask import Flask, json, Response, request,jsonify
from flask_pymongo import PyMongo

from BackEnd.Datos import transporte_datos as datos_transporte, algoritmo_dijkstra, viaje_datos as datos_viaje

app = Flask(__name__)

#conexión a la base de datos
app.config['MONGO_DBNAME'] = 'tribot'
app.config['MONGO_URI'] = 'mongodb://tribot:tribot@ds157390.mlab.com:57390/tribot'

mongo = PyMongo(app)

#guarda la consulta más reciente de una ruta
info_temporal = {}

@app.route('/user',methods=['GET'])
def user():
    user = mongo.db.users
    user.insert({'name':'John'})
    return 'agregado'

@app.route('/destinos',methods=['GET'])
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

    punto_inicio = request.json["partida"]
    punto_destino = request.json["destino"]


    #guarda en una variable el resultado del algoritmo
    ruta_mas_corta = algoritmo_dijkstra.dijkstra(algoritmo_dijkstra.grafo,punto_inicio,punto_destino,nodosVisitados, distancia, nodoAnterior)

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

#prueba temporal para visualizar el contenido de los arreglos
@app.route('/tarifa', methods=['POST'])
def ejemplo_1():

    try:
        transporte_seleccionado = request.json['transporte']
        punto_inicio = request.json["partida"]
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
            pasaje_total = pasaje.TarifaBus(punto_inicio,punto_destino,distancia)

            duracion = datos_viaje.Datos_Duracion()
            duracion_estimada = duracion.duracionBus(distancia)

            for bus in ejecutar_db.find():
                buses.append(
                    {"compania": bus["compania"], "conductor": bus["conductor"], "capacidad": bus["capacidad"],"horarios": bus["horarios"],"contacto": bus["contacto"] })


            json_ruta = (
            {'Distancia': info_temporal[0]['Distancia'], 'Ruta': (info_temporal[0]['Ruta']), 'Transporte': "Bus",
             'Duracion': duracion_estimada, 'Pasaje': pasaje_total,'Buses_disponibles':buses})
            resultado = json.dumps(json_ruta)
            respuesta = Response(resultado, status=200, mimetype='application/json')

        if transporte_seleccionado == "Tren":

            print()

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