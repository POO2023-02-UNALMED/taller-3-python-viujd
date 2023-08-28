class Control:

    def __init__(self):
        self._tv=None

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv._volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)
        