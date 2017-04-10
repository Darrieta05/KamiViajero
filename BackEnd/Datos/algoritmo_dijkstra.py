#algoritmo
grafo = {'1': {'2': 47.2, '3': 70},
         '2': {'1': 47.2, '3': 69.3, '5': 28.6},
         '3': {'1': 70, '2': 69.3, '4': 58.4, '5': 54.7, '8':50},
         '4': {'8': 83.8, '3': 58.4, '25': 100},
         '5': {'2': 28.6, '3': 54.7, '6': 89.9},
         '6': {'5': 89.9, '7': 91.3, '8': 111},
         '7': {'6': 91.3, '8': 92, '9': 108, '23': 106},
         '8': {'4': 83.8, '6': 111, '7': 92, '9': 110, '3':50},
         '9': {'7': 108, '8': 110, '10': 73.8, '24': 32.2},
         '10': {'9': 73.8, '11': 25.2, '22': 60.9},
         '11': {'10': 25.2, '12': 72.5, '13': 83.4, '24': 10},
         '12': {'11': 72.5, '13': 20, '14': 55.4},
         '13': {'11': 83.4, '12': 20, '22': 152},
         '14': {'12': 55.4, '17': 99, '18': 72.41, '24': 22},
         '15': {'16': 70, '24': 140},
         '16': {'15': 70, '17': 95, '26': 140},
         '17': {'14': 99, '16': 95, '18': 60},
         '18': {'14': 72.41, '17': 60, '19': 121.32},
         '19': {'18': 121.32, '21': 39.80, '26': 150.4},
         '20': {'21': 24.1},
         '21': {'19': 39.80, '20': 24.1, '22': 100},
         '22': {'10': 60.9, '13': 152, '21': 100, '23': 180},
         '23': {'7': 106, '22': 180},
         '24': {'9': 32.2, '11': 10, '15': 140, '25': 120, '14': 22},
         '25': {'4': 100, '24': 120},
         '26': {'16': 140, '19': 150.4}
        }

def dijkstra(grafo,inicio, destino, nodosVisitados, distancia, nodoAnterior):

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

            Distancia_total = distancia

            return ({'Ruta': (ruta[::-1]), 'Distancia': round(Distancia_total[destino],2)})

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
            return dijkstra(grafo,punto_auxiliar, destino, nodosVisitados, distancia, nodoAnterior)


'''
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
'''