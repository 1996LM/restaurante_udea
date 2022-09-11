from restaurant_sistem.database_service.generic_database import GenericDataBase

class EmpleadosDataBase(GenericDataBase):
    """Genera la base de datos de los empleados.

    Args:
        GenericDataBase (_type_): Recibe la base de datos generica para generar la base de datos de los empleados.
    """
    def __init__(self) -> None:
        super().__init__(database_name = "empleados")