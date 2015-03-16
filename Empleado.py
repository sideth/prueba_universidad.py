__author__ = 'sidethdj15'
import Lista_Enlazada


class Empleado():
    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

        def __str__(self):
            return
            "Codigo= "+self.codigo+" Nombre= "+self.nombre+" Edad= "+str(self.edad)


class Principal():

    lista = Lista_Enlazada()
    e1 = Empleado("66tgwebh", "Sideth", 19)
    lista.adicionar(e1)
    lista.consultar()