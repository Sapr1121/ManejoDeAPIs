from sodapy import Socrata
import pandas as pd


def socrata(n,dep):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=n, departamento_nom=dep)
    df = pd.DataFrame.from_records(results)
    datos = {"Ciudad":[], "Departamento":[], "Edad":[], "Tipo":[], "Estado":[], "Pais de Origen":[]}
    for MiniDatos in results:
        x = "edad" in MiniDatos

        datos['Ciudad'].append(MiniDatos['ciudad_municipio_nom'])
        datos['Departamento'].append(MiniDatos['departamento_nom'])
        datos['Edad'].append(MiniDatos['edad'])
        datos['Tipo'].append(MiniDatos['fuente_tipo_contagio'])
        datos['Estado'].append(MiniDatos['estado'])
        if ("pais_viajo_1_nom" in MiniDatos):
            datos['Pais de Origen'].append(MiniDatos['pais_viajo_1_nom'])
        else:
            datos['Pais de Origen'].append("")

    df = pd.DataFrame.from_records(datos)
    #print("{}".format(df.to_string(index=False)))
    return df
