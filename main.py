from argparse import ArgumentParser, Namespace
# esta libreria ayuda a definir argumenos que le puedo pasar a un programa

from restaurant_sistem import (
    ClientesDataBase,
    EmpleadosDataBase,
    SedesDataBase,
    ProveedoresDataBase,
    metricas_cliente,
    metricas_empleados 
)
from restaurant_sistem.database_service.proveedores import ProveedoresDataBase
from restaurant_sistem.database_service.sedes import SedesDataBase  


def execute(args , Namespace)->None:
    database  = None
    if args.database_name == "clientes":
        database = ClientesDataBase()
    if args.database_name == "empleados":
        database == EmpleadosDataBase()    
    if args.database_name == "proveedores":
        database == ProveedoresDataBase()  
    if args.database_name == "sedes":
        database = SedesDataBase()
    while True:
        # clientes : nombre, edad, telefono, numero_factura, mes, costo, propina
        # empleados: nombre, edad, telefono, numero_cuenta, mes, total_dias_trabajados,  sueldo.
        #provedores: nombre, producto, telefono, numero_cuenta, mes, cantidad, valor_unidad.
        #la letra c identifica clientes,  e identifica empleados, p identifica provedores,
        #  m identifica menus y s identifica sedes
        #no se si una de las entidades tiene mas datos que sucede
        user_input = input("Ingrese los datos de necesarios:")
        rol, nombre_or_direccion, edad_or_producto, numero_celular,numero_factura_or_cuenta_or_servicios, mes, costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo, propina_or_salario_or_valor_unidad_or_impuestos = user_input.split(" ")

        
        if rol == "s":
            clientes_id = database.create({
            "direccion": nombre_or_direccion,
            "producto": int(edad_or_producto),
            "numero_celular": int(numero_celular),
            "servicios": int(numero_factura_or_cuenta_or_servicios),
            "mes": int(mes),
            "valor_arriendo": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "impuestos": float(propina_or_salario_or_valor_unidad_or_impuestos)
            })
            metricas_sedes(database)

        if rol == "c":
            clientes_id = database.create({
            "nombre": nombre_or_direccion,
            "edad": int(edad_or_producto),
            "numero_celular": int(numero_celular),
            "numero_factura": int(numero_factura_or_cuenta_or_servicios),
            "mes": int(mes),
            "costo": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "propina": float(propina_or_salario_or_valor_unidad_or_impuestos)
            })
            metricas_cliente(database)

        if rol == "p":
            proveedores_id = database.create({
            "nombre": nombre_or_direccion,
            "producto": int(edad_or_producto),
            "numero_celular": int(numero_celular),
            "cuenta": int(numero_factura_or_cuenta_or_servicios),
            "mes": int(mes),
            "cantidad": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "valor_unidad": float(propina_or_salario_or_valor_unidad_or_impuestos)
            })
            metricas_proveedores(database)    


        if rol == "e":
            empleados_id = database.create({
            "nombre": nombre_or_direccion,
            "edad": int(edad_or_producto),
            "numero_celular": int(numero_celular),
            "cuenta": int(numero_factura_or_cuenta_or_servicios),
            "mes": int(mes),
            "total_dias_trabajados": float(costo_or_total_dias_trabajados_or_cantidad_or_valor_arriendo),
            "salario": float(propina_or_salario_or_valor_unidad_or_impuestos)
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

