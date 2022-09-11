def get_costo_total(database)->float:
    data = database.get_all_data()

    costo = 0
    for proveedores_data in data.values():
        costo+= proveedores_data["valor_unidad"]*proveedores_data["cantidad"]
    return costo


def metricas_proveedores(database)-> None:
    print(f"El costo total de todas los productos es : {get_costo_total(database)}")
