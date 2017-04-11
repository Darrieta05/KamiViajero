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

    def TarifaBus(self, inicio, destino):

        pasaje = int(0)
        # bus = 8,9,18,24
        if (inicio == '8' and destino == '9') or (inicio == '9' and destino == '8'):#
            pasaje = int(2750)
        if (inicio == '8' and destino == '18') or (inicio == '18' and destino == '8'):#
            pasaje = int(4500)
        if (inicio == '8' and destino == '24') or (inicio == '24' and destino == '8'):#
            pasaje = int(3000)
        if (inicio == '9' and destino == '18') or (inicio == '18' and destino == '9'): #
            pasaje = int(2950)
        if (inicio == '9' and destino == '24') or (inicio == '24' and destino == '9'):#
            pasaje = int(4375)
        if (inicio == '24' and destino == '18') or (inicio == '18' and destino == '24'):
            pasaje = int(2400)

        return pasaje

    def TarifaAvion(self, distancia):

        # avion = 1,25, 23, 24, 22, 26, 7, 15
        kilometroRegular = int(700)

        tarifa_total = int(kilometroRegular * distancia)

        if distancia > 280:
            kilometro = int(500)
            tarifa_total = int(kilometro * distancia)

        return tarifa_total

    def TarifaTren(self, inicio,destino):

        # tren = 24,15, 10
        pasaje = int(0)
        if (inicio == '24' and destino == '15') or (inicio == '15' and destino == '24'):
            pasaje = int(4250)
        if (inicio == '24' and destino == '10') or (inicio == '10' and destino == '24'):
            pasaje = int(3800)
        if (inicio == '15' and destino == '10') or (inicio == '10' and destino == '15'):
            pasaje = int(4675)
        return pasaje



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

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))

        return duracion_estimada

    def duracionTren(self,distancia):
        velocidad_promedio = (55)  # km/h

        tiempo = round((distancia / velocidad_promedio), 2)  # formula para calcular el tiempo

        # pasar el tiempo de decimales a horas y minutos
        horas = int(tiempo)
        minutos = (tiempo * 60) % 60

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))

        return duracion_estimada

    def duracionAvion(self,distancia):
        velocidad_promedio = (500)  # km/h

        tiempo = round((distancia / velocidad_promedio), 2)  # formula para calcular el tiempo

        # pasar el tiempo de decimales a horas y minutos
        horas = int(tiempo)
        minutos = (tiempo * 60) % 60

        # guarda la duracion con formato
        duracion_estimada = str("%d:%02d" % (horas, minutos))

        return duracion_estimada

