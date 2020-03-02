class View:
    def mostrar_contacto(self, contacto):
        print('*********Datos del contacto*********')
        print('Nombre: ', contacto.nombre)
        print('Telfono: ', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Dirección: ', contacto.dir)
        print('*************************************')

    def mostrar_contactos(self, contactos):
        print('********* Contactos***********')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('**********************************')
    
    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'se ha agregado a la base de datos')
    
    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'se ha eliminado a la base de datos')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'se ha modificado correctamente')

    def contacto_ya_existe(self, contacto):
        print('El contacto', contacto.id_contacto, 'ya existe en la base de datos')

    def contacto_no_existe(self, id_contacto):
        print(id_contacto, 'No existe en la base de datos')

    def start(self):
        print('Esta es una prueva de vista')
    
    def end(self):
        print('Hasta la vista')

    def mostrar_cita(self, cita):
        print('*********Datos de la cita*********')
        print('Nombre: ', cita.id_contacto)
        print('Lugar: ', cita.lugar)
        print('Fecha: ', cita.fecha)
        print('Hora: ', cita.hora)
        print('Asunto: ', cita.asunto)
        print('*************************************')

    def mostrar_citas(self, citas):
        print('********* Citas ***********')
        for c in citas:
            print(c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('**********************************')

    def agregar_cita(self, cita):
        print('se ha agregado una cita a la fecha', cita.asunto)
    
    def borrar_cita(self, cita):
        print('se ha eliminado la cita', cita.asunto)

    def actualizar_cita(self, id_cita):
        print(id_cita, 'se ha modificado correctamente')

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'ya existe en la base de datos')

    def cita_no_existe(self, id_cita):
        print(id_cita, 'No existe en la base de datos')
    

    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('6. Buscar cita')
        print('7. Actualizar cita')
        print('8. Borrar cita')
        print('9. Salir')


