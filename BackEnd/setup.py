from setuptools import setup, find_packages
setup(
    name='TriBot',
    version = '1.0',
    description = 'Aplicacion web que implementa dijkstra para encontrar la ruta mas corta, brinda sugerencias de transporte e informacion de tarfijas y duracion estimada',
    author = 'John Brown - Daniel Arrieta',
    packages =find_packages('BackEnd/Datos'),  # include all packages under src
    exclude_package_data={'': ['README.md']},
)