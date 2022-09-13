def get_costo_medio(database)->float:
    """" Esta funcion obtiene el costo promedio de las facturas.

    Args:
        database (_type_): recibe la base de datos de las facturas del restaurante.

    Returns:
        float:  El costo promedio de las facturas.
    """

    data = database.get_all_data()

    mean=0
    for facturas_data in data.values():
        mean += facturas_data["costo"]
    return mean/database.count()


    


def metricas_facturas(database)->None:
    print(f"El costo promedio de las facturas es: {get_costo_medio(database)}")
    print(f"conteo de facturas:{database.count()}")

    