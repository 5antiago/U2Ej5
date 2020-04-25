from Alumnos import Alumnos
class ManejaAlumnos:
    __alumnos = list

    def __init__(self):
        self.__alumnos = []
    def agregaalum(self, alumno):
        if type(alumno) == Alumnos:
            self.__alumnos.append(alumno)
    def modificarinasistenciasmax(self, nuevas):
        Alumnos.modificamaxinas(nuevas)
    def getnombre(self, i):
        return self.__alumnos[i].getnom()
    def getinas(self, i):
        return self.__alumnos[i].getinas()
    def getdiv(self, i):
        return self.__alumnos[i].getdiv()
    def getanio(self, i):
        return self.__alumnos[i].getanio()
    def getmaxinas(self):
        return Alumnos.getmaxinas()
    def getcantclases(self):
        return Alumnos.getcantclases()
    def getcantalumnos(self):
        return len(self.__alumnos)
