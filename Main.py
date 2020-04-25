import csv

from Alumnos import Alumnos

from Manejaalumno import ManejaAlumnos

def Salir(Alumnado):
    pass

def Listaralumnos(Alumnado):
    anio=int(input("Ingrese año: "))
    div=input("Ingrese Divsión: ").upper()
    cant=Alumnado.getcantalumnos()
    print("{0:15} \t {1:10} ".format("Alumno", "Porcentaje"))
    for i in range(cant):
        if Alumnado.getdiv(i) == div and Alumnado.getanio(i) == anio and Alumnado.getinas(i)>=Alumnado.getmaxinas():
            print("{0:15} \t {1:4}%".format(Alumnado.getnombre(i), Alumnado.getinas(i)*100/Alumnado.getcantclases()))

def Modificarinasmax(Alumnado):
    Alumnado.modificarinasistenciasmax(int(input("Ingrese la nueva cantidad: ")))
    print("Modificado Exitosamente")

switcher = {
    0: Salir,
    1: Listaralumnos,
    2: Modificarinasmax,
}

if __name__ == "__main__":
    Alumnado= ManejaAlumnos()
    with open("Registroalumnos.csv") as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            Alumnado.agregaalum(Alumnos(row[0], row[1], row[2], row[3]))
    opcion=1 
    while opcion != 0:
        print(" 1. Listado de Inasistencias \n 2. Modificar inasistencias máximas \n 0. Salir")
        opcion= int(input("Ingrese una opción: "))
        switcher.get(opcion, lambda: print("Opción incorrecta"))(Alumnado)