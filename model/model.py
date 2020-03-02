from .contacto import Contacto
from .cita import Cita


class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def estacita_id(self, id_cita):
        for ci in self.citas:
            if ci.id_cita == id_cita:
                return True, ci
            return False, 0
    
    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
    
        return False, 0

    #Contacto methods
    def agregar_contactos(self, id_contacto, nombre, tel, correo, dir):
        if not self.esta_id(id_contacto)[0]:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c

        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c

    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_dir != '':
                c.dir = n_dir
            return True
        return False

    def borrar_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(c)
            lista_temp=[c for c in self.citas if c.id_contacto==id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True
        return False



    #Cita methods

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.estacita_id(id_cita)[0]:
            ci = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            self.citas.append(ci)
            return True, ci
            
        return False, ci

    def leer_cita(self, id_cita):
        e, ci = self.estacita_id(id_cita)
        if e:
            return ci
        return False

    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, d = self.estacita_id(id_cita)
        if e:
            if n_id_contacto != '':
                d.id_contacto = n_id_contacto
            if n_lugar != '':
                d.lugar = n_lugar
            if n_fecha != '':
                d.fecha = n_fecha
            if n_hora != '':
                d.hora = n_hora
            if n_asunto != '':
                d.asunto = n_asunto
            
            d.id_contacto = n_id_contacto
            d.lugar = n_lugar
            d.fecha = n_fecha
            d.hora = n_hora
            d.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, ci = self.estacita_id(id_cita)
        if e:
            self.citas.remove(ci)
            return True, ci
        return False, ci
    
    def buscar_citas(self):
           
        findfecha = False
        guessfecha = input('Dame una fecha (dd/mm/aaaa): ')

        for cit in self.citas:
            if guessfecha == cit.fecha:
                print(cit.asunto)
                findfecha = True

        if findfecha == False:
            print('No hay ninguna cita en esta fecha')

    def leer_todos_contactos(self):
        return self.contactos

    def leer_todas_citas(self):
        return self.citas

    def leer_contacto_letra(self, letra):
        #lista=[c for c in self.contactos if c.nombre.lower().startwith(letra.lower())]
        lista=[]
        for c in self.contactos:
            if c.nombre[0].lower()== letra.lower():
                lista.append(c)
        return lista

    def leer_citas_fecha(self, fecha):
        lista=[c for c in self.citas if c.fecha==fecha]
        #lista=[]
        #for c in self.citas:
        #    if c.fecha.append(c)
        return lista