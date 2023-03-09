from sodapy import Socrata
import pandas as pd


def socrata(n,dep):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=n, departamento_nom=dep)
    df = pd.DataFrame.from_records(results)
    datos = {"Ciudad":[], "Departamento":[], "Edad":[], "Tipo":[], "Estado":[]}
    for MiniDatos in results:
        datos['Ciudad'].append(MiniDatos['ciudad_municipio_nom'])
        datos['Departamento'].append(MiniDatos['departamento_nom'])
        datos['Edad'].append(MiniDatos['edad'])
        datos['Tipo'].append(MiniDatos['fuente_tipo_contagio'])
        datos['Estado'].append(MiniDatos['estado'])
    df = pd.DataFrame.from_records(datos)
    print("{}".format(df.to_string(index=False)))