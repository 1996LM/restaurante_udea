class GenericDataBase:

    def __init__(self, database_name: str)->None:  #simplemente una clase que recibe el nombre de la base de datos
        
        self.name = database_name

        self.data = {}  #diccionario
        self.id_counter = 0
    
    def create(self, data: dict)->int:#podria pasar en ves del identificador la cedula (en ves de data dedula)
        """ Este metodo agrega un registro en la base de datos y returna su ID.

        Args:
            data (dict): Dato asociado al objeto

        Returns:
            int: ID de el objeto
        """
        self.data[self.id_counter] = data
        self.id_counter += 1

        return self.id_counter -1
    
    def read(self, _id:int)->dict:
        """ Lee los datos asocidos a un objeto.

        Args:
            _id (int): ID del objeto 

        Returns:
            dict: los datos asociados a ese ID
        """
        return self.data[_id]

    def update(self, _id, data)->None:
        """Cambia los datos asociados a un ID en el diccionario

        Args:
            _id (_type_): ID del objeto 
            data (_type_): Datos del objeto que quiero actualizar
        """
        self.data[_id] = data


    def delete(self, _id: int)->None:
        """Borra la entrada del diccionario

        Args:
            _id (int): ID del objeto 
        """
        del self.data[_id]

    def get_all_data(self)->dict:#retorna la base de datos
        """Obtiene todos los datos de disponibles.

        Returns:
            dict: La base de datos.
        """
        return self.data

    def count(self)->int:
        """Cuenta cuantos datos hay en la base de datos

        Returns:
            int: conteo de los datos
        """
        #cuenta los datos
        return len(self.data)
                      
