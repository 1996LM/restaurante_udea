from restaurant_sistem.database_service.generic_database import GenericDataBase
"""Genera la base de datos de las sedes del restaurante.

    Args:
        GenericDataBase (_type_): Recibe la base de datos genérica. 
    """

class FacturasDataBase(GenericDataBase):
    def __init__(self) -> None:
        super().__init__(database_name = "facturas")