document.getElementById('selectAll').addEventListener('change', function() {
    const checkboxes = document.querySelectorAll('input[name="docentes"]');
    checkboxes.forEach(cb => cb.checked = this.checked);
});

document.getElementById('btnEnviar').addEventListener('click', async function() {
    const seleccionados = document.querySelectorAll('input[name="docentes"]:checked');
    const mensaje = document.getElementById('mensaje').value.trim();

    if (seleccionados.length === 0) {
        alert("Selecciona al menos un docente.");
        return;
    }

    if (!mensaje) {
        alert("Escribe un mensaje antes de enviarlo.");
        return;
    }

    const docentes = Array.from(seleccionados).map(cb => ({
        id: cb.value,
        celular: cb.dataset.numero
    }));

    // 🔹 Abre WhatsApp para cada número seleccionado
    for (const d of docentes) {
        const url = `https://wa.me/51${d.celular.replace(/\s+/g, '')}?text=${encodeURIComponent(mensaje)}`;
        window.open(url, '_blank');
    }

    // 🔹 Registrar mensaje en la base de datos
    try {
        const resp = await fetch('/mensajes/guardar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ docentes, mensaje })
        });

        if (resp.ok) {
            alert("✅ Mensajes enviados y registrados correctamente.");
            document.getElementById('mensaje').value = "";
            seleccionados.forEach(cb => cb.checked = false);
        } else {
            alert("Error al registrar los mensajes en el servidor.");
        }
    } catch (error) {
        console.error(error);
        alert("No se pudo conectar con el servidor.");
    }
});
