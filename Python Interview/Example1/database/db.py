import psycopg2

# Se crea la tabla users en la base de datos ya creada en PostgreSQL y para eso se instala psycopg2 que es un adaptador de base de datos PostgreSQL para Python
# donde por medio de codigo se pueden crear tablas, insertar datos, hacer consultas, etc.
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                email_validated INTEGER DEFAULT 0,
                confirmation_code TEXT
            )
        ''')
        conn.commit()
        print("Tabla 'users' creada exitosamente.")
        conn.close()
    except psycopg2.Error as e:
        print(f"No se pudo crear la tabla: {e}")

# Se insertan datos en la tabla users 
def insert_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, email, email_validated, confirmation_code)
            VALUES (%s, %s, %s, %s)
        ''', ('Ludmila', 'ludmicher6@gmail.com', 0, '123456'))
        conn.commit()
        print("Datos insertados correctamente.")
    except psycopg2.Error as e:
        print(f"No se pudo insertar datos: {e}")
