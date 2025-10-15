from flask import Flask, render_template
from flask_mail import Mail 
import os
import mysql.connector
from controlador_docente import docente_bp
from controlador_inicial import inicio_bp
from control_mensajes import mensajes_bp
from cumpleanios_docentes_controller import cumple_docente_bp
from mail_config import mail 

def create_app():
    app= Flask(__name__)
    
    # Configuración de Mail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'eduardo.diaz@mastersystem.edu.pe'
    app.config['MAIL_PASSWORD'] = 'bsrf haof atug voar'  # contraseña de aplicación de Google
    app.config['MAIL_DEFAULT_SENDER'] = 'eduardo.diaz@mastersystem.edu.pe'


    # Inicializar Mail
    mail.init_app(app)
    
    app.secret_key = os.urandom(24)
    app.register_blueprint(docente_bp)
    app.register_blueprint(inicio_bp)
    app.register_blueprint(mensajes_bp)
    app.register_blueprint(cumple_docente_bp)
    return app
    
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)                                                                                                                                                                                                                                                                                                                                                 