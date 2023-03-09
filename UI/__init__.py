from api import socrata

def atencion():

    dep = input("Ingrese el nombre del departamento: ")
    while(True):
        try:
            lim = int(input("Ingrese el Limite de registros: "))
            if(lim < 1000):
                break
            print("Error ese numero supera al limite (Limite:1000)")
        except ValueError:
            print("Error el numero tiene que ser un entero")
    socrata(lim,dep.upper())