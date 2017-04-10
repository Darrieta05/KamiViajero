class Datos_Tarifas:

    def TarifaTaxi(self,distancia):

        tarifaBase = int(400)
        kilometroRegular = int(300)
        tarifa_total = int(0)

        # descuento por distancia
        if distancia > 200 and distancia < 400:
            tarifa = tarifaBase + (kilometroRegular * distancia)
            descuento = tarifa * 0.15
            tarifa_total = int(tarifa - descuento)
            print(tarifa)
            print("se aplica 15%")
        elif distancia > 400:
            tarifa = tarifaBase + (kilometroRegular * distancia)
            descuento = tarifa * 0.20
            tarifa_total = int(tarifa - descuento)
            print(tarifa)
            print("se aplica 20%")
        else:
            tarifa = tarifaBase + (kilometroRegular * distancia)
            tarifa_total = int(tarifa)
            print(tarifa)
            print("no se aplica %")
        print(tarifa_total)

        return tarifa_total

    def TarifaBus(self, inicio, destino,distancia):

        tarifaBase = int(400)
        kilometroRegular = int(300)
        tarifa_total = int(0)

        if (inicio == '1' and destino == '2') or (inicio == '2' and destino == '1'):

            pasaje = int(1500)

        if (inicio == '3' and destino == '8') or (inicio == '8' and destino == '3'):

            pasaje = int(3500)

        if (inicio == '2' and destino == '5') or (inicio == '5' and destino == '2'):
            pasaje = int(1500)
        if (inicio == '4' and destino == '8') or (inicio == '8' and destino == '4'):
            pasaje = int(3500)
        if (inicio == '9' and destino == '8') or (inicio == '8' and destino == '9'):
            pasaje = int(4375)
        if (inicio == '7' and destino == '9') or (inicio == '9' and destino == '7'):
            pasaje = int(5150)
        if (inicio == '24' and destino == '9') or (inicio == '9' and destino == '24'):
            pasaje = int(3600)
        if (inicio == '15' and destino == '24') or (inicio == '24' and destino == '15'):
            pasaje = int(5000)
        if (inicio == '24' and destino == '11') or (inicio == '11' and destino == '24'):
            pasaje = int(2100)
        if (inicio == '13' and destino == '22') or (inicio == '22' and destino == '13'):
            pasaje = int(4900)
        if (inicio == '8' and destino == '7') or (inicio == '7' and destino == '8'):
            pasaje = int(2000)
        else:
            pasaje = int(distancia * 15)
        return pasaje

    def TarifaAvion(self, distancia):

        # avion = 1,25, 23, 24, 22, 26, 7, 15
        # tren = 24, 15, 12, 11
        kilometroRegular = int(700)

        tarifa_total = int(kilometroRegular * distancia)

        if distancia > 280:
            kilometro = int(500)
            tarifa_total = int(kilometro * distancia)

        return tarifa_total

    def TarifaTren(self, distancia):
        return



class Datos_Duracion:

    def duracionTaxi(self,distancia):
        velocidad_promedio = (65)  # km/h

        tiempo = round((distancia / velocidad_promedio), 2)  # formula para calcular el tiempo

        # pasar el tiempo de decimales a horas y minutos
        horas = int(tiempo)
        minutos = (tiempo * 60) % 60
        # segundos = (tiempo*3600) % 60

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))
        return duracion_estimada

    def duracionBus(self,distancia):
        velocidad_promedio = (50)  # km/h

        tiempo = round((distancia / velocidad_promedio), 2)  # formula para calcular el tiempo

        # pasar el tiempo de decimales a horas y minutos
        horas = int(tiempo)
        minutos = (tiempo * 60) % 60
        # segundos = (tiempo*3600) % 60

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))

        return duracion_estimada

    def duracionTren(self,distancia):
        velocidad_promedio = (55)  # km/h

        tiempo = round((distancia / velocidad_promedio), 2)  # formula para calcular el tiempo

        # pasar el tiempo de decimales a horas y minutos
        horas = int(tiempo)
        minutos = (tiempo * 60) % 60
        # segundos = (tiempo*3600) % 60

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))

        return duracion_estimada

    def duracionAvion(self,distancia):
        velocidad_promedio = (500)  # km/h

        tiempo = round((distancia / velocidad_promedio), 2)  # formula para calcular el tiempo

        # pasar el tiempo de decimales a horas y minutos
        horas = int(tiempo)
        minutos = (tiempo * 60) % 60
        # segundos = (tiempo*3600) % 60

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))

        return duracion_estimada