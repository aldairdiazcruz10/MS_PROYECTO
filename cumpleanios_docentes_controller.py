from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from database import Database
from datetime import date, timedelta
from flask_mail import Message
from mail_config import mail
from controlador_docente import docente_bp

cumple_docente_bp = Blueprint('cumple_docente', __name__)

def get_docentes_cumple_proximo(dias=7):
    """Devuelve lista de docentes que cumplen años dentro de los próximos 'dias'."""
    db = Database()
    cursor = db.get_cursor()
    if not cursor:
        return []

    query = """
        SELECT id, primer_nombre, primer_apellido, fecha_nacimiento
        FROM docentes
        WHERE fecha_nacimiento IS NOT NULL
    """
    cursor.execute(query)
    docentes = cursor.fetchall()
    cursor.close()

    hoy = date.today()
    proximos = []

    for d in docentes:
        fnac = d["fecha_nacimiento"]
        if not fnac:
            continue

        proximo_cumple = fnac.replace(year=hoy.year)
        if proximo_cumple < hoy:
            proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)

        dias_restantes = (proximo_cumple - hoy).days

        if dias_restantes <= dias:
            proximos.append({
                "nombre": f"{d['primer_nombre']} {d['primer_apellido']}",
                "dias_restantes": dias_restantes
            })

    return proximos


@cumple_docente_bp.route("/cumpleaños")
def listar_cumpleaños():
    db = Database()
    cursor = db.get_cursor()
    if not cursor:
        return "Error de conexión a la base de datos", 500

    query = """
        SELECT id, primer_nombre, primer_apellido, correo_institucional, fecha_nacimiento
        FROM docentes
        WHERE fecha_nacimiento IS NOT NULL
    """
    cursor.execute(query)
    docentes = cursor.fetchall()
    cursor.close()

    hoy = date.today()
    lista = []

    for d in docentes:
        fnac = d["fecha_nacimiento"]
        # Cumpleaños del docente este año
        if not fnac: 
            continue
        proximo_cumple = fnac.replace(year=hoy.year)
        if proximo_cumple < hoy:
            proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)

        dias_faltantes = (proximo_cumple - hoy).days

        # Definir color o barra según los días
        if dias_faltantes <= 3:
            color = "danger"  # rojo
        elif dias_faltantes <= 7:
            color = "warning"  # amarillo
        else:
            color = "success"  # verde

        lista.append({
            "id": d["id"],
            "nombre": f"{d['primer_nombre']} {d['primer_apellido']}",
            "correo": d["correo_institucional"],
            "fecha_nacimiento": fnac.strftime("%d-%m-%Y"),
            "dias_faltantes": dias_faltantes,
            "color": color
        })

    lista.sort(key=lambda x: x["dias_faltantes"])

    return render_template("cumple_docentes.html", docentes=lista)


@cumple_docente_bp.route("/cumpleaños/enviar", methods=["POST"])
def enviar_saludo_cumple():
    docente_id = request.form.get("docente_id")
    mensaje_personalizado = request.form.get("mensaje")

    db = Database()
    cursor = db.get_cursor()
    if not cursor:
        return jsonify({"success": False, "error": "Error de conexión"}), 500

    cursor.execute("SELECT primer_nombre, correo_institucional FROM docentes WHERE id = %s", (docente_id,))
    docente = cursor.fetchone()
    cursor.close()

    if not docente:
        return jsonify({"success": False, "error": "Docente no encontrado"}), 404

    nombre = docente["primer_nombre"]
    correo = docente["correo_institucional"]

    # 💌 Mensaje HTML con diseño
    html_message = f"""
        <html>
        <body style="font-family: 'Segoe UI', Arial, sans-serif; text-align: center; background-color: #f8f9fa; padding: 30px;">
            <div style="background-color: white; padding: 30px; border-radius: 15px; 
                        box-shadow: 0px 4px 12px rgba(0,0,0,0.1); max-width: 600px; margin: auto;">
                
                
                
                <h2 style="color: #004AAD; margin-bottom: 10px;">
                    🎉 ¡Feliz cumpleaños, <strong>{nombre}</strong>! 🎂
                </h2>
                
                <p style="font-size: 17px; color: #333; line-height: 1.6; margin-bottom: 20px;">
                    {mensaje_personalizado}
                </p>

                <p style="font-size: 16px; color: #444; line-height: 1.6; margin-top: 20px;">
                    En este día especial, deseamos que la alegría y la inspiración llenen tu vida.  
                    Que sigas alcanzando metas, compartiendo conocimiento y dejando huellas positivas en todos los que te rodean. 🌟
                </p>

                <hr style="margin: 25px 0; border: none; border-top: 2px solid #eee;">

                <p style="font-size: 15px; color: #666;">
                    Con mucho cariño,<br>
                    💙 <strong>La familia Master System</strong>
                </p>
            </div>
        </body>
    </html>

    """

    msg = Message(
        subject=f"🎂 ¡Feliz cumpleaños {nombre}!",
        sender="tu_correo@gmail.com",
        recipients=[correo],
        html=html_message
    )

    try:
        mail.send(msg)
        return jsonify({"success": True, "message": f"Correo enviado a {nombre}"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500