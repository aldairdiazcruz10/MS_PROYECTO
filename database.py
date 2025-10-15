import mysql.connector

class Database:
    _instance = None 
    
    def __new__(cls):
        if cls._instance is None: 
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connect_to_db()
        return cls._instance
    
    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ms_proyecto'
            )
        except mysql.connector.Error as err:
            print(f"Error al  conectar con la base de datos: {err}")
            self.connection  = None     
    
    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            print("reconectando a la base de datos ")
            self.connect_to_db()
        return self.connection
    
    def get_cursor(self):
        """Retorna un uevo cursor si la conexion esta activida"""
        connection = self.get_connection()
        if connection: 
            return connection.cursor(dictionary=True)
        else:
            print("Error: no se puede obtener un cursor la conexcion esta cerrada")
            return None 