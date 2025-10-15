function abrirModalCorreo(id, nombre) {
    document.getElementById('docente_id').value = id;
    document.getElementById('nombreDocente').textContent = nombre;
    let modal = new bootstrap.Modal(document.getElementById('modalCorreo'));
    modal.show();
}

// Elementos
const inputImagenes = document.getElementById('imagenes');
const previewContainer = document.getElementById('previewContainer');

// Mostrar vista previa múltiple
function mostrarPreview(files) {
    previewContainer.innerHTML = '';
    if (files.length > 0) {
        previewContainer.classList.remove('d-none');
        Array.from(files).forEach(file => {
            const img = document.createElement('img');
            img.src = URL.createObjectURL(file);
            img.className = 'img-thumbnail shadow-sm';
            img.style.width = '100px';
            img.style.height = '100px';
            img.style.objectFit = 'cover';
            previewContainer.appendChild(img);
        });
    } else {
        previewContainer.classList.add('d-none');
    }
}

// Cuando se seleccionan imágenes
inputImagenes.addEventListener('change', (e) => {
    mostrarPreview(e.target.files);
});

// Permitir pegar varias imágenes (Ctrl + V)
document.addEventListener('paste', (event) => {
    const items = event.clipboardData.items;
    const dataTransfer = new DataTransfer();

    // Añadimos las imágenes ya seleccionadas (si las hay)
    Array.from(inputImagenes.files).forEach(file => dataTransfer.items.add(file));

    // Agregamos las nuevas imágenes pegadas
    for (let item of items) {
        if (item.type.indexOf("image") !== -1) {
            const file = item.getAsFile();
            dataTransfer.items.add(file);
        }
    }

    // Actualizamos el input file
    inputImagenes.files = dataTransfer.files;
    mostrarPreview(inputImagenes.files);
});

// Envío del formulario
document.getElementById('formCorreo').addEventListener('submit', async function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    const res = await fetch('/docentes/enviar_correo', {
        method: 'POST',
        body: formData
    });

    const result = await res.json();

    if (result.success) {
        alert("✅ Correo enviado correctamente");
        this.reset();
        previewContainer.classList.add('d-none');
        previewContainer.innerHTML = '';
        bootstrap.Modal.getInstance(document.getElementById('modalCorreo')).hide();
    } else {
        alert("❌ Error al enviar: " + (result.error || 'Inténtalo de nuevo'));
    }
});


function limpiarModal(){
    document.getElementById('formCorreo').reset();
    inputImagenes.value='';
    previewContainer.innerHTML='';
    previewContainer.classList.add('d-none');
}


document.getElementById('modalCorreo').addEventListener('hidden.bs.modal',limpiarModal);