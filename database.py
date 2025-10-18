import os
import psycopg

class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connect_to_db()
        return cls._instance
    
    def connect_to_db(self):
        try:
            database_url = os.getenv("DB_URL")  # Render lee esta variable
            self.connection = psycopg.connect(database_url, autocommit=True)
            print("✅ Conexión exitosa a PostgreSQL (Neon)")
        except Exception as err:
            print(f"❌ Error al conectar con la base de datos: {err}")
            self.connection = None
    
    def get_connection(self):
        if self.connection is None or self.connection.closed != 0:
            print("♻️ Reconectando a la base de datos...")
            self.connect_to_db()
        return self.connection
    
    def get_cursor(self):
        connection = self.get_connection()
        if connection:
            # En psycopg3 se usa .cursor() directamente, para obtener dicts:
            return connection.cursor(row_factory=psycopg.rows.dict_row)
        else:
            print("⚠️ Error: no se puede obtener un cursor, la conexión está cerrada")
            return None
