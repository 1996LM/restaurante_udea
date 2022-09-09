def get_edad_media(database)->float:
    data = database.get_all_data()

    mean=0
    for customers_data in data.values():
        mean += customers_data["edad"]
    return mean/database.count()


def get_costo_medio(database)->float:
    data = database.get_all_data()

    mean=0
    for customers_data in data.values():
        mean += customers_data["costo"]
    return mean/database.count()

def visitas_mes(database):
    data = database.get_all_data()

    visitas_por_mes = {}
    for customers_data in data.values():
        if customers_data in visitas_por_mes:
            visitas_por_mes[customers_data]+=1
        else:
            visitas_por_mes[customers_data]=0
    return visitas_por_mes
    

def visitas_mes_promedio(database):
    data = database.get_all_data()
    numero_mes = visitas_mes(data)
    tatal = 0

    for i in numero_mes.values():
        total += i

    return total/12 

def metricas_cliente(database)-> None:
    print(f"Edad mmedia de los clientes : {get_edad_media(database)}")
    print(f"Ccosto medio de las compras de los clientes : {get_costo_medio(database)}")
    print(f"Numero de veces que el cliente visita el restaurante por mes : {visitas_mes(database)}")
    print(f"Visitas en promedio del cliente por mes : {visitas_mes_promedio(database)}")
    print(f"conteo de clientes:{database.count()}")



