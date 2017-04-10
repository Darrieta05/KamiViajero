# TriBot
Servicio Web que muestra la ruta más rápida de un lugar a otro

##Requisitos:

* Python v3.4+
* Flask 0.12
* MongoDB (mlab)
* FrontEnd : Angular2
* Backend host: localhost

Es una aplicación web diseñada con Flask y Angular2 bajo el lenguaje de programacion Python. Consiste en un sistema de
reservación de Transporte, donde dado un punto inicial y un punto de destino, el usuario recibe una ruta optima para su viaje además de sugerencia de transportes y sus tarifas. Se le brinda al usuario una estimación de la duración del viaje.

El sistema permite el registro y login de usuarios, brinda un historial de las rutas solicitadas, además de sugerencias de los mejores destinos, dependiendo de duración, transporte y costo.

Para lograr brindar la una ruta óptima, se trabajó con el algoritmo de Dijsktra, el cual dado un grafo, un punto inicial y punto destino, logra brindar la ruta más corta de un punto a otro. Para el manejo del grafo, se utilizan archivos en formato JSON, para este sistema se utlizan 3 archivos JSON, el primero contiene los id's de los nodos y sus respectivos nodos adyacentes con el valor de sus aristas, el segundo archivo guarda los id's de los nodos junto con sus nombres de destino y el tercer archivo guarda los id's y los transportes que permite cada punto.

Se utiliza la autenticación para asegurar que el usuario se ha "loggeado", de lo contrario, no tendrá acceso al servicio.

Para la base de datos se utiliza Mongodb hosteado en la nube con el servicio de Mlab (https://mlab.com). Se decide utilizar Mongodb como gestor de base de datos ya que es más simple el manejo de JSON.


# Manual de usuario

Click en el siguiente link: https://docs.google.com/document/d/12NO1oWZi0lC5lBbGKFDMdle3eRcUUpCV82TVTnvwO_0/edit?usp=sharing
