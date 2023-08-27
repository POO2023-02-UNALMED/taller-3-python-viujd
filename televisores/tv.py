class TV:
    numTv=0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV()

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca=marca

    def getCanal(self):
        return self._canal
    
    def setCanal(self, Canal):
        self._canal=Canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio (self, precio):
        self._precio=precio
    
    def getVolumen (self):
        return self._volumen
    
    def setVolumen (self, volumen):
        self._volumen=volumen

    def getControl (self):
        return self._control
    
    def setControl (self, control):
        self._control=control

