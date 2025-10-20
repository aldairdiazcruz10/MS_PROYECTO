from flask import Flask, render_template
from flask_mail import Mail 
import os
from controlador_docente import docente_bp
from controlador_inicial import inicio_bp
from control_mensajes import mensajes_bp
from cumpleanios_docentes_controller import cumple_docente_bp
from mail_config import mail 

def create_app():
    app = Flask(__name__)
    
    # Configuración de Mail usando variables de entorno
    app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('mailto:99b357001@smtp-brevo.com')
    app.config['MAIL_PASSWORD'] = os.environ.get('cpTLABJKPS8z6D14')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('eduardo.diaz@mastersystem.edu.pe')

    # Inicializar Mail
    mail.init_app(app)
    
    app.secret_key = os.urandom(24)
    app.register_blueprint(docente_bp)
    app.register_blueprint(inicio_bp)
    app.register_blueprint(mensajes_bp)
    app.register_blueprint(cumple_docente_bp)
    return app

app = create_app()
                                                                                                                                                                                                                                                                                                                               
