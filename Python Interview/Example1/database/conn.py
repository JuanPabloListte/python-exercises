import psycopg2

# En la función connect_db se establece la conexión con la base de datos PostgreSQL
def connect_db():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="PythonInterview",
            user="postgres",
            password="Machupichu1",
            host="localhost",
            port="5432"
        )
        print("Conexion establecida.")
    except psycopg2.Error as e:
        print(f"No se pudo conectar a la base de datos: {e}")
    
    return conn
