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
