def get_arriendo_total(database)->float:
    """Esta funcion calcula el costo del arriendo total pagado por el restaurante

    Args:
        database (_type_): Recibe la base de datos de las sedes de los restaurante.

    Returns:
        float: El costo del arriendo total pagado por el restaurante
    """
    data = database.get_all_data()

    arriendo = 0
    for sedes_data in data.values():
        arriendo += sedes_data["valor_arriendo"]
    return arriendo


def metricas_sedes(database)-> None:
    print(f"El arriendo total de todas las sedes es : {get_arriendo_total(database)}")