def get_edad_media(database)->float:
    """Esta funcion calcula la edad media de los empleados de el restaurante.

    Args:
        database (_type_): Recibe la base de datos de los empleados del restaurante.

    Returns:
        float: La edad media de los empleados del restaurante
    """
    data = database.get_all_data()

    mean=0
    for empleados_data in data.values():
        mean += empleados_data["edad"]
    return mean/database.count()




def get_salario_medio(database)->float:
    """Esat funcion calcula el salario medio de los empleados del restaurante.

    Args:
        database (_type_):Recibe la base de datos de los empleados del restaurante.

    Returns:
        float: El salario medio de los empleados del restaurante.
    """
    data = database.get_all_data()

    mean=0
    for empleados_data in data.values():
        mean += empleados_data["salario"]
    return mean/database.count()



def metricas_empleados(database):
    print("=" * 80)
    print(f"edad media: {get_edad_media(database)}")
    print(f"salario promedio: {get_salario_medio(database)}")
    
