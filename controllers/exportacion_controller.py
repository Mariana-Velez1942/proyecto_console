import json
import csv
from datos.estado import hojas_de_vida
from controllers.utilidades import convertir_sets_a_listas

def exportar_json():
    nombre_archivo = input("Nombre de archivo JSON (sin extensión): ")
    with open(nombre_archivo + ".json", "w", encoding="utf-8") as f:
        serializable = {
            str(k): convertir_sets_a_listas(v) for k, v in hojas_de_vida.items()
        }
        json.dump(serializable, f, indent=4, ensure_ascii=False)
    print(f"✅ Exportado correctamente a {nombre_archivo}.json")

def exportar_csv():
    nombre_archivo = input("Nombre de archivo CSV (sin extensión): ")
    with open(nombre_archivo + ".csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Documento", "Correo", "Habilidades"])
        for hv in hojas_de_vida.values():
            writer.writerow([hv["nombre"], hv["documento"], hv["correo"], ", ".join(hv["habilidades"])])
    print(f"✅ Exportado correctamente a {nombre_archivo}.csv")
