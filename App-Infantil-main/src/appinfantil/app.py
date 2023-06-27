import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from toga.widgets import *
import cv2
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
    def mostrar_ventana_principal(self, widget, tipo_usuario):
        # Mostrar la ventana principal
        self.main_window.show()

#-------------------------
#-------------------------

    # Función que se ejecuta al presionar el botón de login
    def login(self, widget):
        # Obtener el usuario y la contraseña ingresados por el usuario
        usuario = widget.parent.children[1].value
        contrasena = widget.parent.children[3].value
        #llamar a la funcion validar_login con los parametros usuario y contraseña
        if self.validar_login(usuario, contrasena, widget)==True:
            # Ocultar la ventana de login
            widget.parent.parent.hide()
            # oculatar la ventana principal
            self.main_window.hide()
            #ocultar la ventana de login
            widget.parent.parent.hide()
            #llamar a la funcion mostrar_ventana_inicio
            self.mostrar_ventana_inicio(widget)
        #si el usuario y la contraseña son incorrectos enviara un mensaje de error
        else:
            #crear ventana de error
            ventana_error = toga.Window(title="Error", size=(400, 200))
            #crear caja para contener el mensaje de error
            caja_error = toga.Box(style=Pack(direction=COLUMN, padding=5))
            #crear label con el mensaje de error
            label_error = toga.Label('Usuario o contraseña incorrectos', style=Pack(padding=(0, 5)))
            #crear boton de aceptar al presionarlo se cierra la ventana de error
            boton_aceptar = toga.Button('Aceptar', on_press=ventana_error.close)
            
            #agregar el label y el boton a la caja de error
            caja_error.add(label_error)
            caja_error.add(boton_aceptar)
            #la ventana de error contiene pertenece a la clase Appinfantil
            ventana_error.app = self
            #mostrar la caja de error en la ventana de error
            ventana_error.content = caja_error
            #mostrar la ventana de error
            ventana_error.show()


#-------------------------
#-------------------------
    #funcion que valida el usuario y la contraseña
    def validar_login(self, usuario, contrasena, widget):
        #los usuarios y contraseñas correctos estan en una base de datos
        #en este caso se usan valores de ejemplo
        #crear una lista con los usuarios y contraseñas correctos
        usuarios = ['usuario', 'profesor']
        contrasenas = ['contraseña', 'profesor']
        #lista que contiene los usuarios y contraseñas correctos
        usuarios_correctos = list(zip(usuarios, contrasenas))
        #recorrer la lista de usuarios y contraseñas correctos
        for usuario_correcto in usuarios_correctos:
            #si el usuario y la contraseña son correctos retorna True
            if usuario == usuario_correcto[0] and contrasena == usuario_correcto[1]:
                return True
        #si el usuario y la contraseña son incorrectos retorna False
        return False
#-------------------------
#-------------------------
#funcion que muestra la ventana de inicio
    def mostrar_ventana_inicio(self, widget):
            #crear ventana de inicio
            ventana_inicio = toga.Window(title="Inicio", size=(400, 200))
            #añadir boton de leer QR
            boton_qr = toga.Button('Leer QR', on_press=self.mostrar_ventana_qr)
            ventana_inicio.content = boton_qr
            #al presionar el boton de leer QR se llama a la funcion mostrar_ventana_qr
            boton_qr.on_press = functools.partial(self.mostrar_ventana_qr, widget)
            #-------------------------
            #crear boton de ver colección
            boton_coleccion = toga.Button('Ver colección', on_press=self.mostrar_ventana_coleccion)
            ventana_inicio.content = boton_coleccion
            #al presionar el boton de ver colección se llama a la funcion mostrar_ventana_coleccion
            boton_coleccion.on_press = functools.partial(self.mostrar_ventana_coleccion, widget)
            #-------------------------
            # Crear botón de logout para volver a la ventana de login y agregarlo a la caja de login
            boton_logout = toga.Button('Atrás', on_press=self.mostrar_ventana_login)
            ventana_inicio.content = boton_logout

            # Mostrar la ventana de inicio
            ventana_inicio.show()

#-------------------------
#-------------------------
#cree la funcion mostrar_ventana_qr
    def mostrar_ventana_qr(self, widget):
        #crear ventana de qr
        ventana_qr = toga.Window(title="QR", size=(400, 200))
        #crear boton de atrás
        boton_atras = toga.Button('Atrás', on_press=self.mostrar_ventana_inicio)
        ventana_qr.content = boton_atras
        #al presionar el boton de atrás se llama a la funcion mostrar_ventana_inicio
        boton_atras.on_press = functools.partial(self.mostrar_ventana_inicio, widget)
        #mostrar boton de leer qr y llama a la funcion leer_qr
        boton_qr = toga.Button('Leer QR', on_press=self.leer_qr)
        ventana_qr.content = boton_qr
        #al presionar el boton de leer qr se llama a la funcion leer_qr
        boton_qr.on_press = functools.partial(self.leer_qr, widget)
        #crear boton para leer otro codigo qr
        boton_otro_qr = toga.Button('Leer otro QR', on_press=self.leer_qr)
        ventana_qr.content = boton_otro_qr
        #al presionar el boton de leer otro qr se llama a la funcion leer_qr
        boton_otro_qr.on_press = functools.partial(self.leer_qr, widget)

        # Mostrar la ventana de qr
        ventana_qr.show()
#-------------------------
#-------------------------

#cree la funcion leer_qr
    def leer_qr(self, widget):
        #preguntar si desea leer un qr desde la camara o la galeria
        widget.parent.parent.info_dialog('Leer QR', '¿Desea leer un QR desde la cámara o la galería?')
        #crear boton de camara
        boton_camara = toga.Button('Cámara', on_press=self.mostrar_ventana_camara)
        widget.parent.parent.content = boton_camara
        #al presionar el boton de camara se enciende la camara
        boton_camara.on_press = functools.partial(self.mostrar_ventana_camara, widget)
        #comienza a buscar un codigo qr para leer con la camara
        widget.parent.parent.info_dialog('Leer QR', 'Buscando código QR')
        #si se encuentra un codigo qr se muestra un mensaje de exito
        widget.parent.parent.info_dialog('Leer QR', 'Código QR encontrado')
        #se lee el contenido del codigo qr
        widget.parent.parent.info_dialog('Leer QR', 'Contenido del código QR: ')
        #agrega el contenido del codigo qr a la lista de codigos qr
        widget.parent.parent.info_dialog('Leer QR', 'Código QR agregado a la lista')
        
        #se pregunta si desea leer otro codigo qr
        widget.parent.parent.info_dialog('Leer QR', '¿Desea leer otro código QR?')
        #crear boton de si
        boton_si = toga.Button('Si', on_press=self.leer_qr)
        widget.parent.parent.content = boton_si
        #al presionar el boton de si se llama a la funcion leer_qr
        boton_si.on_press = functools.partial(self.leer_qr, widget)
        #crear boton de no
        boton_no = toga.Button('No', on_press=self.mostrar_ventana_inicio)
        widget.parent.parent.content = boton_no
        #al presionar el boton de no se llama a la funcion mostrar_ventana_inicio
        boton_no.on_press = functools.partial(self.mostrar_ventana_inicio, widget)

        #crear boton de galeria
        boton_galeria = toga.Button('Galería', on_press=self.mostrar_ventana_galeria)
        widget.parent.parent.content = boton_galeria
        #al presionar el boton de galeria se abre la galeria
        boton_galeria.on_press = functools.partial(self.mostrar_ventana_galeria, widget)
        #seleccionar un codigo qr de la galeria
        widget.parent.parent.info_dialog('Leer QR', 'Seleccione un código QR de la galería')
        #si se selecciona un codigo qr se muestra un mensaje de exito
        widget.parent.parent.info_dialog('Leer QR', 'Código QR seleccionado')
        #se lee el contenido del codigo qr
        widget.parent.parent.info_dialog('Leer QR', 'Contenido del código QR: ')
        #agrega el contenido del codigo qr a la lista de codigos qr
        widget.parent.parent.info_dialog('Leer QR', 'Código QR agregado a la lista')
        #se pregunta si desea leer otro codigo qr
        widget.parent.parent.info_dialog('Leer QR', '¿Desea leer otro código QR?')
        #crear boton de si
        boton_si = toga.Button('Si', on_press=self.leer_qr)
        widget.parent.parent.content = boton_si
        #al presionar el boton de si se llama a la funcion leer_qr
        boton_si.on_press = functools.partial(self.leer_qr, widget)
        #crear boton de no
        boton_no = toga.Button('No', on_press=self.mostrar_ventana_inicio)
        widget.parent.parent.content = boton_no
        #al presionar el boton de no se llama a la funcion mostrar_ventana_inicio
        boton_no.on_press = functools.partial(self.mostrar_ventana_inicio, widget)

        #crear boton de atrás
        boton_atras = toga.Button('Atrás', on_press=self.mostrar_ventana_inicio)
        widget.parent.parent.content = boton_atras
        #al presionar el boton de atrás se llama a la funcion mostrar_ventana_inicio
        boton_atras.on_press = functools.partial(self.mostrar_ventana_inicio, widget)

def main():
    return Appinfantil('appinfantil', 'org.pybee.appinfantil')

if __name__ == '__main__':
    main().main_loop()