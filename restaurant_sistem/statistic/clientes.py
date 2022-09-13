def get_edad_media(database)->float:
    """Esta función calcula la edad media de los clientes del restaurante.

    Args:
        database (_type_): recibe la base de datos de los clientes del restaurante.

    Returns:
        float: La edad media de los clientes del restaurante
    """
    data = database.get_all_data()

    mean=0
    for clientes_data in data.values():
        mean += clientes_data["edad"]
    return mean/database.count()


def get_costo_medio(database)->float:
    """" Esta funcion obtiene el costo medio de las compras realizadas por los clientes.

    Args:
        database (_type_): recibe la base de datos de los clientes del restaurante.

    Returns:
        float:  La costo media de las compras realizadas por los  clientes del restaurante.
    """

    data = database.get_all_data()

    mean=0
    for clientes_data in data.values():
        mean += clientes_data["costo"]
    return mean/database.count()

def visitas_mes(database):
    """Esta funcion calcula el numero total de vicitas que tuvo el restaurante al mes.

    Args:
        database (_type_): Recibe la base de datos de los clientes del restaurante.

    Returns:
        _type_: Un diccionario con el numero total de visitas por cada mes del año
    """
    data = database.get_all_data()

    visitas_por_mes = {}
    for clientes_data in data.values():
        if clientes_data in visitas_por_mes:
            visitas_por_mes[clientes_data]+=1
        else:
            visitas_por_mes[clientes_data]=0
    return visitas_por_mes
    

def visitas_mes_promedio(database):
    """Esta funcion calcula el numero de visitas realizadas en promedio por mes.

    Args:
        database (_type_): Recibe la base de datos de los clientes del restaurante.

    Returns:
        _type_: Visitas en promedio realizadas por mes
    """
    data = database.get_all_data()
    numero_mes = visitas_mes(data)
    tatal = 0

    for i in numero_mes.values():
        total += i

    return total/12 

def metricas_cliente(database)-> None:
    print(f"Edad mmedia de los clientes : {get_edad_media(database)}")
    print(f"Costo medio de las compras de los clientes : {get_costo_medio(database)}")
    print(f"Numero de veces que el cliente visita el restaurante por mes : {visitas_mes(database)}")
    print(f"Visitas en promedio del cliente por mes : {visitas_mes_promedio(database)}")
    print(f"conteo de clientes:{database.count()}")



