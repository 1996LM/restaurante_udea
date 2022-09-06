from argparse import ArgumentParser

from restaurant_sistem.database_service.customers import CustomersDataBase

def execute(args):
    customers_database = CustomersDataBase(database_name=args.database_name)

    while True:
        # nombre, edad, telefono, numero_factura
        user_input = input("ingrese los datos del cliente:")
        name, age, phone_number, invoice_number = user_input.split(" ")

        print(name)
        print(age)
        print(phone_number)
        print(invoice_number)

def main():
    parser = ArgumentParser()

    parser.add_argument(
        "-dn", "--database.name", type = str, 
        choices = ["sedes", "empleados","clientes", "proveedores", "productos", "menus"]
    )
    args = parser.parse_args()
    execute(args)



if __name__ == "__main__":
    main()


