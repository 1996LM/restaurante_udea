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


def get_servicios_total(database)->float:
    """Esta funcion calcula el costo total de  servicios  pagado por el restaurante

    Args:
        database (_type_): Recibe la base de datos de las sedes de los restaurante.

    Returns:
        float: El costo de servicios total pagado por el restaurante
    """
    data = database.get_all_data()

    servicios = 0
    for sedes_data in data.values():
        servicios += sedes_data["servicios"]
    return servicios


def get_impuestos_total(database)->float:
    """Esta funcion calcula el costo total de  impuestos  pagado por el restaurante

    Args:
        database (_type_): Recibe la base de datos de las sedes de los restaurante.

    Returns:
        float: El costo de impuestos total pagado por el restaurante
    """
    data = database.get_all_data()

    impuestos = 0
    for sedes_data in data.values():
        impuestos += sedes_data["impuestos"]
    return impuestos


def metricas_sedes(database)-> None:
    print(f"El arriendo total de todas las sedes es : {get_arriendo_total(database)}")
    print(f"El total de servicios pagados por todas las sedes es : {get_servicios_total(database)}")
    print(f"El total de impuestos pagados por todas las sedes es : {get_impuestos_total(database)}")