from flask import Blueprint, render_template
from cumpleanios_docentes_controller import get_docentes_cumple_proximo
inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route("/")
def index():
    proximos_cumples = get_docentes_cumple_proximo(7)
    total_proximos = len(proximos_cumples)

    return render_template("index.html", proximos_cumples=proximos_cumples, total_proximos=total_proximos)
