from restaurant_sistem.database_service.generic_database import GenericDataBase

class SedesDataBase(GenericDataBase):
    def __init__(self) -> None:
        super().__init__(database_name = "sedes")