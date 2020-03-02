from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

"""Contactos=[]
c=Contacto(1,'Fernando Salinas', '419-100-1138','fernando@gmail.com','Dr. Mora, Gto')
c2=Contacto(2,'Juan Perez', '423-990-9876','juan@gmail.com','Salamanca, Gto')    

"""
#ci=Cita(1,1, 'Jardin Princial', '18-02-2020', '15:30', 'Sin Asunto')

"""print(c.nombre)
print(c.id_contacto)
print(c.tel)
print(c.dir)"""

"""ne=True
Contactos.append(c)
Contactos.append(c2)

gess=input('Dame un Nombre: ')

for c in Contactos:
    if gess.lower() == c.nombre.lower():
        print('Si esta')
        break
else:
    print('No esta')
"""
#for i in range(2):
#    if gess == Contactos[i].nombre:
#        print('este contacto existe')
#        ne=False
#        break
#if ne:
#    print('este contacto no existe')
"""
m=Model()
m.agregar_contactos(1,'Fernando Salinas', '419-100-1138','fernando@gmail.com','Dr. Mora, Gto')
m.agregar_contactos(2,'Juan Perez', '423-990-9876','juan@gmail.com','Salamanca, Gto')
m.agregar_contactos(3,'Pedro Hernandez', '8787-132-9777','perdroh@hotmail.com','Guanajuato, Gto')

s=m.leer_todos_contactos()

for c in s:
    print(c.nombre)

n=Model()
n.agregar_cita(1,1, 'Jardin Princial', '18-02-2020', '15:30', 'Sin Asunto')

r=n.leer_cita(1)
print(r.lugar)



s=m.leer_todos_contactos()
for c in s:
    print(c.nombre)
"""
cont=Controller()
cont.start()
