from restaurant_sistem.database_service.generic_database import GenericDataBase

class ProveedoresDataBase(GenericDataBase):
    def __init__(self) -> None:
        super().__init__(database_name = "proveedores")