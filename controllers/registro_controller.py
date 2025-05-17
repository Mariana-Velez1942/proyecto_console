from datos.estado import hojas_de_vida, correos_registrados, habilidades_globales
from datetime import datetime

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