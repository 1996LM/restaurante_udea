from restaurant_sistem.database_service.generic_database import GenericDataBase

class ClientesDataBase(GenericDataBase):
    def __init__(self) -> None:
        super().__init__(database_name = "clientes")