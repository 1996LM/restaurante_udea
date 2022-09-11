def get_arriendo_total(database)->float:
    data = database.get_all_data()

    arriendo = 0
    for sedes_data in data.values():
        arriendo += sedes_data["valor_arriendo"]
    return arriendo


def metricas_sedes(database)-> None:
    print(f"El arriendo total de todas las sedes es : {get_arriendo_total(database)}")