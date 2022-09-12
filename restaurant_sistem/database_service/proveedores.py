from restaurant_sistem.database_service.generic_database import GenericDataBase

"""Genera la base de datos de los proveedores.

    Args:
        GenericDataBase (_type_): Recibe la base de datos genérica. 
    
"""

class ProveedoresDataBase(GenericDataBase):
    def __init__(self) -> None:
        super().__init__(database_name = "proveedores")