import toga
from toga.style import Pack
from toga.style.pack import COLUMN
#from toga.widgets import carousel ,label,button,box
from toga.widgets import *
from toga.constants import LEFT, RIGHT
from toga.android.widgets.camera import CameraView
import time
import functools
import pyzbar.pyzbar as pyzbar

class Appinfantil(toga.App):
    def startup(self):
        # Crear la ventana principal
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Crear botones para elegir tipo de usuario al presionarlos se llama a la funcion mostrar_ventana_login
        boton_estudiante = toga.Button('Estudiante', on_press=functools.partial(self.mostrar_ventana_login, 'Estudiante'))
        boton_profesor = toga.Button('Profesor', on_press=functools.partial(self.mostrar_ventana_login, 'Profesor'))

        # Agregar los botones a la ventana principal
        self.main_window.content = toga.Box(children=[boton_estudiante, boton_profesor])

        # Mostrar la ventana principal
        self.main_window.show()
#-------------------------
#-------------------------        
    def mostrar_ventana_login(self, tipo_usuario, widget):
        # Ocultar la ventana principal
        self.main_window.hide()

        # Crear la ventana de login
        ventana_login = toga.Window(title="Login - {}".format(tipo_usuario), size=(400, 200))

        # la ventana pertenece a la clase Appinfantil
        ventana_login.app = self

        #crear caja para para contener los campos de usuario y contraseña
        caja_login= toga.Box(style=Pack(direction=COLUMN, padding=5))

        #en la caja_login se agregan los campos de usuario y contraseña
        caja_login.add(toga.Label('Usuario:', style=Pack(padding=(0, 5))))
        caja_login.add(toga.TextInput(style=Pack(padding=(0, 5))))
        caja_login.add(toga.Label('Contraseña:', style=Pack(padding=(0, 5))))
        caja_login.add(toga.PasswordInput(style=Pack(padding=(0, 5))))

        #añadir placeholder a los campos de usuario y contraseña
        caja_login.children[1].placeholder = 'Ingrese su usuario'
        caja_login.children[3].placeholder = 'Ingrese su contraseña'
        
        #crear botón de login y agregarlo a la caja de login
        boton_login = toga.Button('Login', on_press=self.login)
        caja_login.add(boton_login)
        
        # Crear botón de atrás para volver a la ventana principal y agregarlo a la caja de login
        boton_atras = toga.Button('Atrás', on_press=self.mostrar_ventana_principal)
        caja_login.add(boton_atras)

        #mostar la caja de login en la ventana de login
        ventana_login.content = caja_login

        # Mostrar la ventana de login
        ventana_login.show()

#-------------------------
#-------------------------
    def mostrar_ventana_principal(self, widget):
        # Mostrar la ventana principal
        self.main_window.show()

#-------------------------
#-------------------------
#cambio test2
    # Función que se ejecuta al presionar el botón de login
    def login(self, widget):
        # Obtener el usuario y la contraseña ingresados por el usuario
        usuario = widget.parent.children[1].value
        contrasena = widget.parent.children[3].value
        #llamar a la funcion validar_login con los parametros usuario y contraseña
        if self.validar_login(usuario, contrasena):
            # Ocultar la ventana de login
            widget.visible = False
            #llamar a la funcion mostrar_ventana_inicio
            self.mostrar_ventana_inicio(widget)
        #si el usuario y la contraseña son incorrectos enviara un mensaje de error
        else:
            #mostrar mensaje de error
            self.main_window.info_dialog('Error', 'Usuario o contraseña incorrectos')
            
#-------------------------
#-------------------------
    #funcion que valida el usuario y la contraseña
    def validar_login(self,usuario, contraseña):
    # Diccionario de usuarios y contraseñas asignadas
        usuarios = {
        'admin': 'password_admin',
        'usuario1': '123456',
        'usuario2': 'qwerty'
    }

    # Verificar si el usuario y la contraseña coinciden con los valores del diccionario
        if usuario in usuarios and contraseña == usuarios[usuario]:
            return True
        else:
            return False

#-------------------------
#-------------------------
#funcion que muestra la ventana de inicio
    def mostrar_ventana_inicio(self, widget):
            #crear ventana de inicio
            ventana_inicio = toga.Window(title="Inicio", size=(400, 200))
            #la ventana pertenece a la clase Appinfantil
            ventana_inicio.app = self
            # Crear los botones
            boton_qr = toga.Button('Leer QR', on_press=self.mostrar_ventana_qr)
            boton_coleccion = toga.Button('Ver colección', on_press=self.mostrar_ventana_coleccion)
            boton_logout = toga.Button('Cerrar sesión', on_press=self.mostrar_ventana_principal)

            # Crear una caja y agregar los botones a la caja
            caja = toga.Box()
            caja.add(boton_qr)
            caja.add(boton_coleccion)
            caja.add(boton_logout)

            # Asignar la caja como contenido de la ventana
            ventana_inicio.content = caja

            # Mostrar la ventana de inicio
            ventana_inicio.show()
#-------------------------
#-------------------------
#cree la funcion mostrar_ventana_coleccion
    def mostrar_ventana_coleccion(self, widget):
        #mostrar ventana de coleccion
        ventana_coleccion = toga.Window(title="Colección", size=(400, 200))
        #la ventana pertenece a la clase Appinfantil
        ventana_coleccion.app = self
        #mostrar 4 listas desplegables
        #primera lista desplegable Matematicas
        lista_matematicas = toga.Selection(items=['Matematicas', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        ventana_coleccion.content = lista_matematicas
        #segunda lista desplegable Lenguaje
        lista_lenguaje = toga.Selection(items=['Lenguaje', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        ventana_coleccion.content = lista_lenguaje
        #tercera lista desplegable Ciencias
        lista_ciencias = toga.Selection(items=['Ciencias', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        ventana_coleccion.content = lista_ciencias
        #cuarta lista desplegable Ingles
        lista_ingles = toga.Selection(items=['Ingles', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        ventana_coleccion.content = lista_ingles
        #crear boton de atrás
        boton_atras = toga.Button('Atrás', on_press=self.mostrar_ventana_inicio)
        ventana_coleccion.content = boton_atras
#-------------------------
#-------------------------
#cree la funcion mostrar_ventana_qr
    def mostrar_ventana_qr(self, widget):
         # Crear ventana de QR
        ventana_qr = toga.Window(title="QR", size=(400, 200))
        ventana_qr.app = self

        # Crear los botones
        boton_atras = toga.Button('Atrás', on_press=self.mostrar_ventana_inicio)
        boton_qr = toga.Button('Leer QR', on_press=self.leer_qr)
        boton_otro_qr = toga.Button('Leer otro QR', on_press=self.leer_qr)

        # Crear una caja y agregar los botones a la caja
        caja = toga.Box()
        caja.add(boton_atras)
        caja.add(boton_qr)
        caja.add(boton_otro_qr)

        # Asignar la caja como contenido de la ventana
        ventana_qr.content = caja

        # Mostrar la ventana de QR
        ventana_qr.show()
#-------------------------
#-------------------------

#cree la funcion leer_qr
    def leer_qr(self, frame):
        # Buscar códigos QR en el fotograma
        codigos = pyzbar.decode(frame)

        # Procesar los códigos QR encontrados
        for codigo in codigos:
            # Extraer el contenido del código QR
            contenido = codigo.data.decode('utf-8')

            # Imprimir el contenido del código QR
            print('Código QR encontrado:', contenido)

            # Mostrar los contenidos QR en forma de carrusel
            self.mostrar_contenidos_qr(contenido)

        # Actualizar el visor de cámara con el fotograma procesado
        self.camera_view.update_image(frame)

        # Detener la captura de video después de leer 5 códigos QR
        if len(codigos) >= 5:
            self.camera_view.stop_capture()
    # -------------------------
    #  -------------------------
    
    def mostrar_contenidos_qr(self, contenido_qr):
        # Crear una ventana para mostrar el carrusel
        ventana_carrusel = toga.Window(title="Carrusel de Contenidos QR", size=(600, 400))

        # Crear un carrousel para mostrar los contenidos
        carrousel = Carousel()

        # Crear una etiqueta con el contenido del código QR
        etiqueta = Label(contenido_qr)

        # Agregar la etiqueta al carrousel
        carrousel.add(etiqueta)

        # Crear botones de navegación izquierda y derecha para el carrousel
        boton_izquierda = Button('<')
        boton_derecha = Button('>')

        # Configurar las acciones de los botones de navegación
        def ir_a_izquierda(widget):
            carrousel.select_previous()

        def ir_a_derecha(widget):
            carrousel.select_next()

        boton_izquierda.on_press = ir_a_izquierda
        boton_derecha.on_press = ir_a_derecha

        # Crear una caja para contener los botones de navegación
        caja_botones = Box(children=[boton_izquierda, boton_derecha], style=Pack(direction=LEFT))

        # Crear una caja para contener el carrousel y los botones de navegación
        caja_principal = Box(children=[carrousel, caja_botones], style=Pack(direction=RIGHT))

        # Agregar la caja principal al contenido de la ventana del carrusel
        ventana_carrusel.content = caja_principal

        # Mostrar la ventana del carrusel
        ventana_carrusel.show()

def main():
    return Appinfantil('appinfantil', 'org.pybee.appinfantil')

if __name__ == '__main__':
    main().main_loop()