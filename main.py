from argparse import ArgumentParser, Namespace

from restaurant_sistem import (
    ClientesDataBase,
    EmpleadosDataBase,
    metricas_cliente,
    metricas_empleados 
)  


def execute(args , Namespace)->None:
    database  = None
    if args.database_name == "clientes":
        database = ClientesDataBase()
    if arg.database_name == "empleados":
        database == EmpleadosDataBase()    
    while True:
        # clientes : nombre, edad, telefono, numero_factura, mes, costo, propina
        # empleados: nombre, edad, telefono, numero_cuenta, mes, total_dias_trabajados,  sueldo.
        #la letra c identifica clientes y la letra e a empleados
        #no se si una de las entidades tiene mas datos que sucede
        user_input = input("Ingrese los datos del cliente:")
        rol, nombre, edad, numero_celular,numero_factura_or_cuenta, mes, costo_or_total_dias_trabajados, propina_or_salario= user_input.split(" ")

        if rol == "c":
            clientes_id = database.create({
            "nombre": nombre,
            "edad": int(edad),
            "numero_celular": int(numero_celular),
            "numero_factura": int(numero_factura_or_cuenta),
            "mes": int(mes),
            "costo": float(costo_or_total_dias_trabajados),
            "propina": float(propina_or_salario)
            })
            metricas_cliente(database)


        if rol == "e":
            clientes_id = database.create({
            "nombre": nombre,
            "edad": int(edad),
            "numero_celular": int(numero_celular),
            "cuenta": int(numero_factura_or_cuenta),
            "mes": int(mes),
            "total_dias_trabajados": float(costo_or_total_dias_trabajados),
            "salario": float(propina_or_salario)
            })
            metricas_empleados(database)
        
        
def main()->None:
    parser = ArgumentParser()

    parser.add_argument(
        "-dn", "--database-name", type = str, 
        choices = ["sedes", "empleados","clientes", "proveedores", "productos", "menus"]
    )
    args = parser.parse_args()
    execute(args)
    
    
if __name__ == "__main__":
    main()

