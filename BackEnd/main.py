from flask import Flask
from flask import Flask, request, jsonify, json, Response

app = Flask(__name__)

grafo = {'1': {'2': 67.2 , '3': 90},
             '2': { '1': 67.2 , '3': 69.3 , '5': 28.6},
             '3': { '1': 90 , '2': 69.3, '4': 58.4 , '5': 54.7},
             '4': { '8': 83.8 ,  '3': 58.4 , '25': 116},
             '5': { '2': 28.6 , '3': 54.7 , '6': 89.9},
             '6': { '5': 89.9 , '7': 91.3 , '8': 111},
             '7': { '6': 91.3 , '8': 113 , '9': 125 , '23': 106},
             '8': { '4': 83.8 , '6': 111 , '7': 113 , '9': 157},
             '9': { '7': 125 , '8': 157 , '10': 73.8, '24': 48.2},
             '10':{ '9': 73.8, '11': 45.2 , '22': 80.9},
             '11':{ '10': 45.2 , '12': 72.5, '13': 83.4, '24': 39},
             '12':{ '11': 72.5, '13': 20 , '14': 55.4 },
             '13':{ '11': 83.4, '12': 20 , '22': 152},
             '14':{ '12': 55.4, '17': 99 , '18': 72.41},
             '15':{ '16': 70 , '24': 174},
             '16':{ '15': 70 , '17': 95 , '26': 190},
             '17':{ '14': 99 , '16': 95 , '18': 60},
             '18':{ '14': 72.41 , '17': 60 , '19': 121.32},
             '19':{ '18': 121.32, '21': 39.80 , '26': 175.4},
             '20':{ '21': 24.1},
             '21':{ '19': 39.80,  '20': 24.1, '22': 176},
             '22':{ '10': 80.9 , '13': 152 , '21': 176 , '23': 220},
             '23':{ '7': 106 , '22': 220},
             '24':{ '9': 48.2 , '11': 39 , '15': 174 , '25': 163},
             '25':{ '4': 116 ,  '24': 163},
             '26':{ '16': 190 , '19': 175.4}
             }

destinos = {'1': 'Parque Nacional Santa Rosa, Provincia de Guanacaste',
            '3': 'Parque Nacional Palo Verde, Provincia de Guanacaste, Bagaces',
            '2': 'Parque Nacional Rincón de la Vieja, Provincia de Guanacaste',
            '4': 'Parque Nacional Barra Honda',
            '5': 'Volcán Miravalles',
            '6': 'Parque Nacional Volcán Tenorio ',
            '7': 'Parque Nacional Volcán Arenal',
            '8': 'Monteverde',
            '9': 'Parque Nacional Volcán Poás',
            '10': 'La Selva Biological Station',
            '11': 'Parque Nacional Braulio Carrillo',
            '12': 'Volcán Irazu',
            '13': 'Parque Nacional Volcán Turrialba',
            '14': 'Parque Nacional Tapantí -Macizo de la Muerte',
            '15': 'Parque Nacional Manuel Antonio',
            '16': 'Parque Nacional Marino Ballena',
            '17': 'Parque Nacional Los Quetzales',
            '18': 'Parque Nacional Chirripó',
            '19': 'Parque Internacional La Amistad',
            '20': 'Refugio Nacional Gandoca-Manzanillo',
            '21': 'Parque Nacional Cahuita',
            '22': 'Parque Nacional Tortuguero',
            '23': 'Caño Negro Wildlife Refuge',
            '24': 'San José',
            '25': 'Montezuma',
            '26': 'Parque nacional Corcovado'
            }

def dijkstra(grafo, inicio, destino, nodosVisitados=[], distancia={}, nodoAnterior={}):

    if inicio not in grafo:
        return ('EL punto de partida no se encuentra registrado')
    elif destino not in grafo:
        return ('EL punto de destino no se encuentra registrado')
    else:

        if inicio == destino:
            # una vez que el punto inicio sea igual al punto de destino, se recorre el diccionario con los nodos anteriores
            # y se van guardando en la lista de la ruta
            ruta = [] #guarda la ruta más corta
            anterior = destino
            while anterior != None:
                ruta.append(anterior)
                anterior = nodoAnterior.get(anterior, None)

            return ({'Ruta': (ruta[::-1]), 'Distancia': str(distancia[destino])})

        else:
            # si inicio != destino, se ejecuta por primera vez, se inicializa la distancia en 0
            if not nodosVisitados:
                distancia[inicio] = 0

            for nodoAdyacente in grafo[inicio]:
                #se empieza a visitar a los nodos adyacentes al nodo inicial, si aún no han sido visitados
                if nodoAdyacente not in nodosVisitados:
                    #ahora la nueva distancia va a ser = a la suma de la distancia actual + la distancia de la arista del nodo adyacente
                    distancia_actual = distancia[inicio] + grafo[inicio][nodoAdyacente]

                    if distancia_actual < distancia.get(nodoAdyacente, float('inf')):
                        distancia[nodoAdyacente] = distancia_actual
                        nodoAnterior[nodoAdyacente] = inicio

            nodosVisitados.append(inicio)
            nodos_no_visitados = {}

            for nodo in grafo:
                if nodo not in nodosVisitados:
                    nodos_no_visitados[nodo] = distancia.get(nodo, float('inf'))

            punto_auxiliar = min(nodos_no_visitados, key=nodos_no_visitados.get)
            #se ejecuta el metodo recursivamente. Ahora recine como parametro el proximo nodo que no ha sido visitado y
            #con la menor distancia
            return dijkstra(grafo, punto_auxiliar, destino, nodosVisitados, distancia, nodoAnterior)


@app.route('/')
def index():
    #guarda en una variable el resultado del algoritmo
    ruta_mas_corta = dijkstra(grafo, '20', '25')
    #se inicializa la lista que guardará el nombre de los puntos que recorre el algoritmo para llegar al destino
    ruta = []

    #por cada punto guardado en el camino de la ruta mas corta
    #busca el id de la ruta en el json "destinos" para encontrar su nombre correspondiente y lo agrega a la lista
    for destino in ruta_mas_corta['Ruta']:
        ruta.append(destinos[destino])

    #se le da formato el json que se retorna
    json_ruta=({'Distancia':ruta_mas_corta['Distancia'],'Ruta': (ruta[::-1])})
    resultado = json.dumps(json_ruta)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    return respuesta

#prueba temporal para visualizar el contenido de los arreglos
@app.route('/grafo', methods=['GET'])
def ejemplo_1():
    resultado = json.dumps(grafo)
    respuesta = Response(resultado, status=200, mimetype='application/json')
    return respuesta



## Main
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')