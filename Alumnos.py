class Alumnos:
    __nombre = str
    __anio = int
    __div = str
    __inasistencias = int
    max_inasis = 20
    canclases = 60
    def __init__(self, nom, anio, div, inas):
        self.__nombre=nom
        self.__anio = anio
        self.__div = div
        self.__inasistencias = inas
    def getanio(self):
        return int(self.__anio)
    def getdiv(self):
        return str(self.__div)
    def getnom(self):
        return str(self.__nombre)
    def getinas(self):
        return int(self.__inasistencias)
    @classmethod
    def getmaxinas(cls):
        return int(cls.max_inasis)
    @classmethod
    def getcantclases(cls):
        return int(cls.canclases)
    @classmethod
    def modificamaxinas(cls, nuevasinas):
        if type(nuevasinas)==int:
            cls.max_inasis = nuevasinas
