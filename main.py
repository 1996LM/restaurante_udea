from argparse import ArgumentParser

from restaurant_sistem.database_service.customers import CustomersDataBase
from restaurant_sistem.statistic.customers import metricas_cliente


def execute(args):
    customers_database = CustomersDataBase(database_name = args.database_name)
    
    while True:
        # nombre, edad, telefono, numero_factura, mes
        user_input = input("Ingrese los datos del cliente:")
        nombre, edad, numero_celular,numero_factura, mes, costo, propina= user_input.split(" ")

        customers_id = customers_database.create({
            "nombre": nombre,
            "edad": edad,
            "numero_celular": numero_celular,
            "numero_factura": numero_factura,
            "mes": mes,
            "costo": costo,
            "propina": propina

        })
        print(metricas_cliente(customers_database))

def main():
    parser = ArgumentParser()

    parser.add_argument(
        "-dn", "--database-name", type = str, 
        choices = ["sedes", "empleados","clientes", "proveedores", "productos", "menus"]
    )
    args = parser.parse_args()
    execute(args)


if __name__ == "__main__":
    main()



