import psycopg2
import smtplib
import random
import string


# En la función get_users_not_validated se obtienen, mediante psycopg2, los usuarios que no validaron sus correos electrónicos
def get_users_not_validated(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, name, email, confirmation_code
            FROM users
            WHERE email_validated = 0
        ''')
        users = cursor.fetchall()
        return users
    except psycopg2.Error as e:
        print(f"No se pudo obtener los usuarios no validados: {e}")

# En la función send_email_confirmation se envía un correo electrónico al usuario con el código de confirmación
# para que pueda validar su correo electrónico, aca se utiliza la librería smtplib para enviar correos electrónicos
# y se utiliza la librería random para generar un código de confirmación aleatorio
# ademas para configurar el email hay que generar una contraseña de aplicacion en gmail
def send_email_confirmation(user_email, confirmation_code):
    from_email = "juanpilistte@gmail.com"
    from_password = "upgj yyqz zjra zppg"
    to_email = user_email

    subject = "Confirmación de correo electrónico"
    body = f"Por favor, confirma tu correo electrónico con el siguiente código: {confirmation_code}"

    try:
        from_email_ = str(from_email)
        to_email_ = str(to_email)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, from_password)
        body = str(f"Subject: {subject}\n\n{body}")
        server.sendmail(from_email_, to_email_, body.encode('utf-8'))
        server.quit()
        print("Correo enviado exitosamente.")
    except smtplib.SMTPException as e:
        print(f"No se pudo enviar el correo de confirmacion: {e}")

def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))