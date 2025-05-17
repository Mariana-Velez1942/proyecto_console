from collections import Counter
from datos.estado import hojas_de_vida

def filtrar_por_experiencia():
    minimo = int(input("Filtrar por mínimo de años de experiencia: "))
    print("\n--- CANDIDATOS CON MÁS DE", minimo, "AÑOS ---")
    for hv in hojas_de_vida.values():
        total = sum(exp["duracion"] for exp in hv["experiencia"])
        if total >= minimo:
            print(f"{hv['nombre']} - {total} años")

def habilidades_mas_comunes():
    todas = []
    for hv in hojas_de_vida.values():
        todas.extend(hv["habilidades"])
    contador = Counter(todas)
    print("\n--- HABILIDADES MÁS COMUNES ---")
    for habilidad, cantidad in contador.most_common():
        print(f"{habilidad}: {cantidad}")
