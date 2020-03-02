from view.view import View
from model.model import Model

class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View()


    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        b, c=self.model.agregar_contactos(id_contacto, nombre, tel, correo, dir)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)
    
    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c=self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre='', n_tel='', n_correo='', n_dir=''):
        e=self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e,c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contacto_letra(self, letra):
        c=self.model.leer_contacto_letra(letra)
        self.view.mostrar_contactos(c)


    #Citas controllers

    def insertar_contactos(self):
        self.agregar_contacto(1,'Fernando Salinas', '419-100-1138','fernando@gmail.com','Dr. Mora, Gto')
        self.agregar_contacto(2,'Juan Perez', '423-990-9876','juan@gmail.com','Salamanca, Gto')
        self.agregar_contacto(3,'Jose Hernandez', '8787-132-9777','perdroh@hotmail.com','Guanajuato, Gto')

    


    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        b, c=self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if b:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(c)
    
    
    
    def leer_cita(self, id_cita):
        e, ci= self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(ci)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_todas_citas(self):
        ci=self.model.leer_todas_citas()
        self.view.mostrar_citas(ci)
    
    def actuaizar_cita(self, id_cita, n_id_contacto = '', n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        e=self.model.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e,c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas_fecha(self, fecha):
        lista=self.model.leer_citas_fecha(fecha)
        self.view.mostrar_citas(lista)

    def insertar_cita(self):
            self.agregar_cita(1,1, 'Salon 310', '05-03-2020', '14:00', 'Clase de Sistemas de Informacion')
            self.agregar_cita(1,2, 'Salon 310', '02-03-2020', '12:00', 'Clase de Circuitos Electricos')

    def start(self):
        self.view.start()

        self.insertar_contactos()
        self.insertar_cita()
        self.leer_todos_contactos()
        self.leer_contacto_letra('J')
        self.leer_todas_citas()
        self.leer_citas_fecha('02-03-2020')


    def menu(self):
        self.view.menu()
        o= input('Selecciona una opcion (1-9')
        if o=='1':
            id=input('ID: ')
            id=int(id)
            nom=input('Nombre: ')
            tel=input('Telefono(xxx-xxx-xxxx): ')
            correo=input('Correo: ')
            dir=input('Direccion: ')
            self.agregar_contacto(id, nom, tel, correo, dir)
        elif o=='2':
           pass 
        elif o=='3':
            pass
        elif o=='4':
            pass
        elif o=='5':
            pass
        elif o=='6':
            pass
        elif o=='7':
            pass
        elif o=='8':
            pass
        elif o=='9':
            self.view.end()
        else:
            pass

