import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(user='root', password='1234', database='appinfantil', host='127.0.0.1', port='3306', auth_plugin='mysql_native_password')
    if conexion.is_connected():
        print("Conectado a la base de datos")
        infoserver = conexion.get_server_info()
        print("Informacion del servidor: ", infoserver)
except Error as ex:
    print("Error durante la conexion a la base de datos", ex)	
finally:
    if conexion.is_connected():
        conexion.close() # Cerramos la conexion
        print("La conexion ha finalizado")
