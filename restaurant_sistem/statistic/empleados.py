def get_edad_media(database)->float:
    data = database.get_all_data()

    mean=0
    for empleados_data in data.values():
        mean += empleados_data["edad"]
    return mean/database.count()


def get_salario_medio(database)->float:
    data = database.get_all_data()

    mean=0
    for empleados_data in data.values():
        mean += empleados_data["salario"]
    return mean/database.count()

def metricas_empleados(database):
    print("=" * 80)
    print(f"edad media: {get_edad_media(database)}")
    print(f"salario promedio: {get_salario_medio(database)}")
    
