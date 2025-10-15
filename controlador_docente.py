from flask import Flask, Blueprint, send_file, url_for, render_template,redirect,request, flash
from database import Database 
from flask_mail import Mail, Message
import os
import openpyxl
import io
from twilio.rest import Client
from mail_config import mail 
import mimetypes
docente_bp = Blueprint('docente', __name__)

@docente_bp.route("/docentes")
def listar_docentes():
    db = Database()
    cursor = db.get_cursor()
    if cursor:
        cursor.execute("SELECT * FROM docentes")
        docentes = cursor.fetchall()
        cursor.close()
        return render_template("docentes.html", docentes=docentes)
    else:
        return "Error: no se pudo obtener datos de la base de datos", 500
    
@docente_bp.route("/docentes/editar/<int:id>", methods=["POST"])
def editar_docente(id):
    primer_nombre = request.form.get("primer_nombre")
    segundo_nombre = request.form.get("segundo_nombre")
    primer_apellido = request.form.get("primer_apellido")
    segundo_apellido = request.form.get("segundo_apellido")
    correo_institucional = request.form.get("correo_institucional")
    celular = request.form.get("celular")

    db = Database()
    cursor = db.get_cursor()
    if cursor:
        cursor.execute("""
            UPDATE docentes
            SET primer_nombre = %s, segundo_nombre= %s, primer_apellido = %s, segundo_apellido= %s, correo_institucional = %s, celular = %s
            WHERE id = %s
        """, (primer_nombre,segundo_nombre, primer_apellido,segundo_apellido, correo_institucional, celular, id))
        db.connection.commit()
        cursor.close()
        return redirect("/docentes")
    else:
        return "Error: no se pudo actualizar docente", 500

@docente_bp.route("/docentes/agregar", methods =["POST"])
def agregar_docente():
    db=Database()
    cursor = db.get_cursor()
    if cursor:
        data = (
            request.form["dni"],
            request.form["primer_apellido"],
            request.form["segundo_apellido"],
            request.form["primer_nombre"],
            request.form.get("segundo_nombre",""), #se utiliza este metodo por motivos de que puede que no tengo 2 nombres
            request.form["correo_institucional"],
            request.form["celular"]
        )
        
        query = """ INSERT INTO docentes 
        (dni, primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, correo_institucional,
        celular) VALUES (%s, %s, %s, %s, %s, %s, %s)        
        """
        cursor.execute(query, data)
        db.connection.commit()
        cursor.close()
        return redirect(url_for("docente.listar_docentes"))
    else: 
        return "Error: no se pudo conectar a la base de datos", 500
    
@docente_bp.route("/docentes/eliminar/<int:id>", methods=["POST"])
def eliminar_docente(id):
    db = Database()
    cursor = db.get_cursor()
    if cursor:
        try:
            cursor.execute("DELETE FROM docentes WHERE id = %s", (id,))
            db.connection.commit()
            cursor.close()
            return redirect(url_for("docente.listar_docentes"))
        except Exception as e:
            cursor.close()
            return f"Error al eliminar docente: {e}", 500
    else:
        return "Error: no se pudo conectar a la base de datos", 500

@docente_bp.route("/docentes/exportar")
def exportar_docentes():
    db = Database()
    cursor = db.get_cursor()
    if cursor:
        cursor.execute("""
            SELECT dni, primer_apellido, segundo_apellido, primer_nombre, 
                   segundo_nombre, correo_institucional, celular 
            FROM docentes
        """)
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]  # nombres de columnas
        cursor.close()

        import pandas as pd
        from io import BytesIO
        from flask import send_file

        # Si rows está vacío, evita exportar solo cabeceras
        if not rows:
            return "No hay docentes para exportar", 404

        # Asegurarse que rows es lista de tuplas
        if isinstance(rows[0], dict):  # si usas DictCursor
            df = pd.DataFrame(rows)  # pandas ya reconoce dicts
        else:  # si son tuplas normales
            df = pd.DataFrame(rows, columns=column_names)

        # Guardar Excel en memoria
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Docentes")

        output.seek(0)

        return send_file(
            output,
            as_attachment=True,
            download_name="docentes.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        return "Error: no se pudo conectar a la base de datos", 500




UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@docente_bp.route("/docentes/enviar_correo", methods=["POST"])
def enviar_correo_docente():
    docente_id = request.form.get("docente_id")
    mensaje = request.form.get("mensaje")
    imagenes = request.files.getlist("imagenes[]")

    if not docente_id or not mensaje:
        return {"success": False, "error": "Datos incompletos"}, 400

    # 🧩 Obtener correo del docente
    db = Database()
    cursor = db.get_cursor()
    if not cursor:
        return {"success": False, "error": "Error de conexión"}, 500

    cursor.execute("SELECT correo_institucional FROM docentes WHERE id = %s", (docente_id,))
    row = cursor.fetchone()
    cursor.close()

    if not row:
        return {"success": False, "error": "Docente no encontrado"}, 404

    correo = row["correo_institucional"]

    # 🧩 Guardar imágenes temporalmente
    imagen_paths = []
    for img in imagenes:
        if img and img.filename:
            filename = os.path.basename(img.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            img.save(save_path)
            imagen_paths.append(save_path)

    # 🧩 Crear mensaje
    msg = Message(
        subject="📩 Mensaje desde la plataforma",
        sender="tu_correo@gmail.com",
        recipients=[correo]
    )
    msg.body = mensaje

    # 🧩 Adjuntar imágenes (automáticamente detecta tipo MIME)
    for path in imagen_paths:
        mime_type, _ = mimetypes.guess_type(path)
        mime_type = mime_type or "application/octet-stream"
        with open(path, "rb") as f:
            msg.attach(os.path.basename(path), mime_type, f.read())

    # 🧩 Enviar correo
    try:
        mail.send(msg)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}, 500
    finally:
        # 🧩 Eliminar archivos temporales
        for path in imagen_paths:
            if os.path.exists(path):
                os.remove(path)