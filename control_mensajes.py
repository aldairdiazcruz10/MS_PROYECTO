from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from database import Database  # tu clase de conexión

mensajes_bp = Blueprint('mensajes_bp', __name__)

# 🔹 Mostrar la lista de docentes
@mensajes_bp.route('/mensajes', methods=['GET'])
def listar_docentes():
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("SELECT id, primer_nombre, primer_apellido, celular, correo_institucional FROM docentes")
    docentes = cursor.fetchall()
    return render_template('mensajes_docentes.html', docentes=docentes)

# 🔹 Guardar mensajes enviados
@mensajes_bp.route('/mensajes/guardar', methods=['POST'])
def guardar_mensajes():
    data = request.get_json()
    docentes = data.get('docentes', [])
    mensaje = data.get('mensaje', '')

    db = Database()
    cursor = db.get_cursor()

    for d in docentes:
        cursor.execute("""
            INSERT INTO mensajes_docentes (docente_id, mensaje, fecha_envio)
            VALUES (%s, %s, %s)
        """, (d['id'], mensaje, datetime.now()))

    db.connection.commit()
    return jsonify({"status": "ok"})

