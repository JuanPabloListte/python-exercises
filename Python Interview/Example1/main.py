from database.conn import connect_db
from database.db import *
from core.email_validated import *

def main():
    # en el main se realiza la conexion a la base de datos, se obtienen los usuarios no validados con la funcion
    # get_users_not_validated y se le envia un correo de confirmacion
    conn = connect_db()
    if conn:
        # create_table(conn)
        # insert_data(conn)
        unvalidated_users = get_users_not_validated(conn)
        # se recorre la lista de usuarios no validados y se envia un correo de confirmacion a cada uno
        for user in unvalidated_users:
            user_email = user[2]
            confirmation_code = generate_confirmation_code()
            send_email_confirmation(user_email, confirmation_code)
            conn.commit()
        conn.close()
        print('Operaciones completadas exitosamente.')
    else:
        print('Error al conectar con la base de datos.')

if __name__ == "__main__":
    main()