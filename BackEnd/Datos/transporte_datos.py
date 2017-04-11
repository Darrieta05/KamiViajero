# -*- coding: utf-8 *-*
class Info_Rutas:
    #Transportes disponibles dependiendo de su punto



    #avion = 23, 24, 22, 26
    #bus = 8,9,18,24
    #tren = 24,15, 10

    transportes = {  '1': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '2': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '3': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '4': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '5': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '6': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '7': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '8': [{'Taxi':True,'Bus':True,'Tren':False,'Avion':False}],
                    '9': [{'Taxi':True,'Bus':True,'Tren':False,'Avion':False}],
                    '10': [{'Taxi':True,'Bus':False,'Tren':True,'Avion':False}],
                    '11': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '12': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '13': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '14': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '15': [{'Taxi':True,'Bus':False,'Tren':True,'Avion':False}],
                    '16': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '17': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '18': [{'Taxi':True,'Bus':True,'Tren':False,'Avion':False}],
                    '19': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '20': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '21': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '22': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':True}],
                    '23': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':True}],
                    '24': [{'Taxi':True,'Bus':True,'Tren':True,'Avion':True}],
                    '25': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':False}],
                    '26': [{'Taxi':True,'Bus':False,'Tren':False,'Avion':True}],
                }
    #id y nombre del destino (nodos del grafo)
    destinos = {'1': 'Parque Nacional Santa Rosa, Provincia de Guanacaste',
                '2': 'Parque Nacional Rincón de la Vieja, Provincia de Guanacaste',
                '3': 'Parque Nacional Palo Verde, Provincia de Guanacaste, Bagaces',
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

    def habilitaTransporte(self,inicio,destino,transportes=transportes):
        transporteDisponible = []

        #verifica los transportes disponibles en el punto inicial
        puntoInicial_taxi= transportes[inicio][0]['Taxi']
        puntoInicial_bus = transportes[inicio][0]['Bus']
        puntoInicial_avion = transportes[inicio][0]['Avion']
        puntoInicial_tren = transportes[inicio][0]['Tren']

        # verifica los transportes disponibles en el punto destino
        puntoDestino_taxi = transportes[destino][0]['Taxi']
        puntoDestino_bus = transportes[destino][0]['Bus']
        puntoDestino_avion = transportes[destino][0]['Avion']
        puntoDestino_tren = transportes[destino][0]['Tren']

        #compara los valores, si un transporte es "True" en ambos puntos (inicio y destino) agrega el transporte
        #a la lista de "transporteDisponible"
        if (puntoInicial_taxi == True) & (puntoDestino_taxi == True):
            transporteDisponible.append('Taxi')

        if (puntoInicial_bus == True) & (puntoDestino_bus == True):
            transporteDisponible.append('Bus')

        if (puntoInicial_avion == True) & (puntoDestino_avion == True):
            transporteDisponible.append('Avion')

        if (puntoInicial_tren == True) & (puntoDestino_tren == True):
            transporteDisponible.append('Tren')

        return transporteDisponible
