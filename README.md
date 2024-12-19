# eva4_gestion_inventario
sistema de gestión de inventario de productos básico para pequeña tienda o almacén 

prerrequisitos:
instalar python3.12
instalar gitbash

manual de instalación local(windows):

1.- descargamos el proyecto desde github utilizando la terminal, mediante el siguiente comando:
git clone https://github.com/Toussaint20/eva4_gestion_inventario.git

2.-accedemos a la carpeta donde se descargó el sistema y creamos un entorno virtual utilizando la terminal, u opcionalmente la terminal de virtual studio code, mediante el siguiente comando:
python -m venv entorno

3.-activamos el entorno virtual:
.env\scripts\activate

4.- instalamos las librerías necesarias para el sistema:
pip install django djangorestframework djangorestframework-simplejwt requests psycopg2 psycopg2-binary
