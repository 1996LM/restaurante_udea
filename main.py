from argparse import ArgumentParser, Namespace
# esta libreria ayuda a definir argumenos que le puedo pasar a un programa

from restaurant_sistem import(
    ClientesDataBase,
    EmpleadosDataBase,
    SedesDataBase,
    ProveedoresDataBase,
    FacturasDataBase,
    metricas_cliente,
    metricas_empleados ,
    metricas_proveedores,
    metricas_sedes,
    metricas_facturas
)

facturas = open("facturas_clase.txt", "a")
clientes = open("clientes_clase.txt", "a")
empleados = open("empleados_clase.txt", "a")
proveedores = open("proveedores_clase.txt", "a")
sedes = open("sedes_clase.txt", "a")


def execute(args: Namespace )->None:
    database  = None
    if args.database_name == "clientes":
        database = ClientesDataBase()
    if args.database_name == "empleados":
        database == EmpleadosDataBase()    
    if args.database_name == "proveedores":
        database == ProveedoresDataBase()  
    if args.database_name == "sedes":
        database = SedesDataBase()
    if args.database_name == "facturas":
        database == FacturasDataBase
    while True:
        # clientes : nombre, edad, telefono, numero_factura, mes, costo, propina
        # empleados: nombre, edad, telefono, numero_cuenta, mes, total_dias_trabajados,  sueldo.
        #provedores: nombre, producto, telefono, numero_cuenta, mes, cantidad, valor_unidad.
        #la letra c identifica clientes,  e identifica empleados, p identifica provedores,
        #  m identifica menus, f identifica facturas y s identifica sedes
        #no se si una de las entidades tiene mas datos que sucede
        user_input = input("Ingrese los datos necesarios:")
        rol, nombre, edad_or_producto_or_direccion_or_cedula, numero_celular,numero_factura_or_cuenta_or_servicios_or_producto_comprado, mes, costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo, propina_or_salario_or_valor_unidad_or_impuestos_forma_pago = user_input.split(" ")

        if rol == "f":
            facturas_id = database.create({
            "nombre_cliente": nombre,
            "cedula": int(edad_or_producto_or_direccion_or_cedula),
            "numero_celular": int(numero_celular),
            "producto_comprado": int(numero_factura_or_cuenta_or_servicios_or_producto_comprado),
            "fecha": int(mes),
            "costo": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "forma de pago": float(propina_or_salario_or_valor_unidad_or_impuestos_forma_pago)
            })
            #metricas_facturas(database)

        if rol == "s":
            sedes_id = database.create({
            "nombre": nombre,
            "direccion": int(edad_or_producto_or_direccion_or_cedula),
            "numero_celular": int(numero_celular),
            "servicios": int(numero_factura_or_cuenta_or_servicios_or_producto_comprado),
            "mes": int(mes),
            "valor_arriendo": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "impuestos": float(propina_or_salario_or_valor_unidad_or_impuestos_forma_pago)
            })
            metricas_sedes(database)

        if rol == "c":
            clientes_id = database.create({
            "nombre": nombre,
            "edad": int(edad_or_producto_or_direccion_or_cedula),
            "numero_celular": int(numero_celular),
            "numero_factura": int(numero_factura_or_cuenta_or_servicios_or_producto_comprado),
            "mes": int(mes),
            "costo": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "propina": float(propina_or_salario_or_valor_unidad_or_impuestos_forma_pago)
            })

            metricas_cliente(database)

        if rol == "p":
            proveedores_id = database.create({
            "nombre": nombre,
            "producto": int(edad_or_producto_or_direccion_or_cedula),
            "numero_celular": int(numero_celular),
            "cuenta": int(numero_factura_or_cuenta_or_servicios_or_producto_comprado),
            "mes": int(mes),
            "cantidad": int(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "valor_unidad": float(propina_or_salario_or_valor_unidad_or_impuestos_forma_pago)
            })
            metricas_proveedores(database)    


        if rol == "e":
            empleados_id = database.create({
            "nombre": nombre,
            "edad": int(edad_or_producto_or_direccion_or_cedula),
            "numero_celular": int(numero_celular),
            "cuenta": int(numero_factura_or_cuenta_or_servicios_or_producto_comprado),
            "mes": int(mes),
            "total_dias_trabajados": int(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "salario": float(propina_or_salario_or_valor_unidad_or_impuestos_forma_pago)
            })
            metricas_empleados(database)
        
        
def main()->None:
    parser = ArgumentParser()

    parser.add_argument(
        "-dn", "--database-name", type = str, 
        choices = ["sedes", "empleados","clientes", "proveedores", "facturas"]
    )
    args = parser.parse_args()
    execute(args)
    
    
if __name__ == "__main__":
    main()

facturas.close()
clientes.close()
empleados.close
proveedores.close()
sedes.close()

