from argparse import ArgumentParser

from restaurant_sistem.database_service.customers import CustomersDataBase

def execute(args):
    customers_database = CustomersDataBase(database_name = args.database_name)
    
    while True:
        # nombre, edad, telefono, numero_factura, mes
        user_input = input("Ingrese los datos del cliente:")
        name, age, phone_number, invoice_number, mes = user_input.split(" ")

        customers_id = customers_database.create({
            "name": name,
            "age": age,
            "phone_number": phone_number,
            "invoice_number": invoice_number,
            "mes": mes
        })

        print(customers_database.get_all_data())
        print(customers_database.count())

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



