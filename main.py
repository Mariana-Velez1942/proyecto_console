import json
import csv
from datetime import datetime
from collections import Counter

# Datos globales
hojas_de_vida = {}
correos_registrados = set()
habilidades_globales = set()

def calcular_edad(fecha_nacimiento):
    return (datetime.now() - datetime.strptime(fecha_nacimiento, "%Y-%m-%d")).days // 365

def registrar_hoja_vida():
    print("\n--- REGISTRAR HOJA DE VIDA ---")
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    correo = input("Correo electrónico: ")
    if correo in correos_registrados:
        print("❌ Correo ya registrado.")
        return
    contacto = input("Teléfono: ")
    direccion = input("Dirección: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")

    clave = (documento, fecha_nacimiento)

    formacion = []
    while input("¿Agregar formación académica? (s/n): ").lower() == 's':
        institucion = input("  Institución: ")
        titulo = input("  Título: ")
        años = input("  Años: ")
        formacion.append({"institucion": institucion, "titulo": titulo, "años": años})

    experiencia = []
    while input("¿Agregar experiencia laboral? (s/n): ").lower() == 's':
        empresa = input("  Empresa: ")
        cargo = input("  Cargo: ")
        funciones = input("  Funciones: ")
        duracion = int(input("  Duración (años): "))
        experiencia.append({"empresa": empresa, "cargo": cargo, "funciones": funciones, "duracion": duracion})

    referencias = []
    while input("¿Agregar referencia? (s/n): ").lower() == 's':
        nombre_ref = input("  Nombre: ")
        relacion = input("  Relación: ")
        telefono = input("  Teléfono: ")
        referencias.append((nombre_ref, relacion, telefono))

    habilidades = set(input("Habilidades (separadas por comas): ").lower().split(","))
    habilidades = {h.strip() for h in habilidades}
    habilidades_globales.update(habilidades)

    hojas_de_vida[clave] = {
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "contacto": contacto,
        "direccion": direccion,
        "fecha_nacimiento": fecha_nacimiento,
        "formacion": formacion,
        "experiencia": experiencia,
        "referencias": referencias,
        "habilidades": habilidades
    }

    correos_registrados.add(correo)
    print("✅ Hoja de vida registrada exitosamente.")

def buscar_por_documento():
    doc = input("Documento: ")
    fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
    clave = (doc, fecha)
    hv = hojas_de_vida.get(clave)
    if not hv:
        print("❌ No se encontró esa hoja de vida.")
        return
    mostrar_hoja(hv)

def mostrar_hoja(hv):
    print("\n--- HOJA DE VIDA ---")
    for k, v in hv.items():
        print(f"{k.capitalize()}:")
        if isinstance(v, list) or isinstance(v, set):
            for item in v:
                print("  ", item)
        else:
            print(" ", v)

def filtrar_por_experiencia():
    minimo = int(input("Filtrar por mínimo de años de experiencia: "))
    print("\n--- CANDIDATOS CON MÁS DE", minimo, "AÑOS ---")
    for hv in hojas_de_vida.values():
        total = sum(exp["duracion"] for exp in hv["experiencia"])
        if total >= minimo:
            print(f"{hv['nombre']} - {total} años")

def convertir_sets_a_listas(diccionario):
    resultado = {}
    for k, v in diccionario.items():
        if isinstance(v, set):
            resultado[k] = list(v)
        elif isinstance(v, dict):
            resultado[k] = convertir_sets_a_listas(v)
        elif isinstance(v, list):
            resultado[k] = [convertir_sets_a_listas(i) if isinstance(i, dict) else i for i in v]
        else:
            resultado[k] = v
    return resultado

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

def habilidades_mas_comunes():
    todas = []
    for hv in hojas_de_vida.values():
        todas.extend(hv["habilidades"])
    contador = Counter(todas)
    print("\n--- HABILIDADES MÁS COMUNES ---")
    for habilidad, cantidad in contador.most_common():
        print(f"{habilidad}: {cantidad}")

def menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("1. Registrar hoja de vida")
        print("2. Buscar hoja de vida")
        print("3. Filtrar por experiencia")
        print("4. Exportar a JSON")
        print("5. Exportar a CSV")
        print("6. Ver habilidades más comunes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_hoja_vida()
        elif opcion == "2":
            buscar_por_documento()
        elif opcion == "3":
            filtrar_por_experiencia()
        elif opcion == "4":
            exportar_json()
        elif opcion == "5":
            exportar_csv()
        elif opcion == "6":
            habilidades_mas_comunes()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
