class GenericDataBase:

    def __init__(self, database_name: str)->None:  #simplemente una clase que recibe el nombre de la base de datos
        self.name = database_name

        self.data = {}  #diccionario
        self.id_counter = 0
    
    def create(self, data: dict)->int:#podria pasar en ves del identificador la cedula (en ves de data dedula)
        """ Este metodo agrega un registro en la base de datos y returna su ID.

        Args:
            data (dict): Dato asociado al cliente

        Returns:
            int: ID de el cliente
        """
        self.data[self.id_counter] = data
        self.id_counter += 1

        return self.id_counter -1
    
    def read(self, _id:int)->dict:
        return self.data[_id]

    def update(self, _id, data)->None:
        self.data[_id] = data


    def delete(self, _id: int)->None:
        del self.data[_id]

    def get_all_data(self)->dict:#retorna la base de datos
        return self.data

    def count(self)->int:
        #cuenta los datos
        return len(self.data)
                      
