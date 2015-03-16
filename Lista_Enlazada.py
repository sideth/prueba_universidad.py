
class Lista_Enlazada:

    def __init__(self):
        self.raiz = None
        self.final = None
        self.sig = None

    def esta_vacia(self):
        if self.raiz is None and self.final is None:
            return True
        else:
            return False

    def adicionar(self, item):
        if self.esta_vacia():
            self.raiz = item
            self.final = item
        else:
            self.final.sig = item
        self.final = item


    def consultar(self):
        if self.esta_vacia():
            print("Lista Vacia")
        else:
            aux = self.raiz
            while aux is not None:
                print aux
                if aux == self.final:
                    break
                aux = aux.sig

    def eliminar(self, valor):
        anterior = None
        p = self.raiz
        while p is not None and p.valor is not valor:
            anterior = p
            p = p.sig
        if p is None:
            return False
        else:
            anterior.sig = p.sig
            p.sig = None
            return True









