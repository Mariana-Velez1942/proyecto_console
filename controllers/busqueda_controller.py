from datos.estado import hojas_de_vida

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
