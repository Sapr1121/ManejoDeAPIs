from api import socrata
import pandas as pd

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
    df = socrata(lim,dep.upper())
    df = df[["Estado","Edad", "Tipo", "Ciudad", "Departamento", "Pais de Origen",]]
    print(df.to_string(index = False))
