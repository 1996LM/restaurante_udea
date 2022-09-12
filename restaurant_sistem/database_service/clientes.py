from restaurant_sistem.database_service.generic_database import GenericDataBase

class ClientesDataBase(GenericDataBase):
    """Genera la base de datos de los clientes.

    Args:
        GenericDataBase (_type_): Recibe la base de datos genérica.
    """
    def __init__(self) -> None:
        super().__init__(database_name = "clientes")