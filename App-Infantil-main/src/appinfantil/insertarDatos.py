import mysql.connector # Importamos el conector de mysql
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(user='root', password='1234', database='appinfantil', host='127.0.0.1', port='3306', auth_plugin='mysql_native_password')
    if conexion.is_connected():
        print("Conectado a la base de datos")
        cursor=conexion.cursor()
        rut = input("Ingrese el rut del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        fechaNacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
        colegio = input("Ingrese el colegio del alumno: ")
        curso = input("Ingrese el curso del alumno: ")
        correoElectronico = input("Ingrese el correo electronico del alumno: ")
        sentencia = "INSERT INTO alumno (rut, nombre, apellido, fechaNacimiento, colegio, curso, correoElectronico) VALUES ('"+rut+"','"+nombre+"','"+apellido+"','"+fechaNacimiento+"','"+colegio+"','"+curso+"','"+correoElectronico+"')"
        cursor.execute(sentencia)
        # cursor.execute("INSERT INTO alumno (rut, nombre, apellido, fechaNacimiento, colegio, curso, correoElectronico) VALUES ('123456789','Juanito','Perez','2010-01-01','Jose Miguel Infante','Septimo','juanito@gmail.com')")
        conexion.commit() # Guardamos los cambios
        print("Registro guardado con exito")
except Error as ex:
    print("Error durante la conexion a la base de datos", ex)	
finally:
    if conexion.is_connected():
        conexion.close() # Cerramos la conexion
        print("La conexion ha finalizado")
