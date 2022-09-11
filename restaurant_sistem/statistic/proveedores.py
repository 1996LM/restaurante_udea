def get_costo_total(database)->float:
    """Esta funcion calcula el costo total de un producto a un proveedor.

    Args:
        database (_type_): Recibe la base de datos de los proveedores del restaurante.


    Returns:
        float: El costo total de un producto a un proveedor.

    """
    data = database.get_all_data()

    costo = 0
    for proveedores_data in data.values():
        costo+= proveedores_data["valor_unidad"]*proveedores_data["cantidad"]
    return costo


def metricas_proveedores(database)-> None:
    print(f"El costo total de todas los productos es : {get_costo_total(database)}")
