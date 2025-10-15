// Variables globales
        let currentDocenteId = null;
        
        // Inicialización
        document.addEventListener('DOMContentLoaded', function() {
            // Búsqueda en tiempo real
            document.getElementById('searchInput').addEventListener('input', function() {
                searchDocentes(this.value);
            });
        });

        // Función de búsqueda
        function searchDocentes(searchTerm) {
            const tableBody = document.getElementById('docentesTableBody');
            const rows = tableBody.querySelectorAll('tr');
            const noResults = document.getElementById('noResults');
            let visibleRows = 0;

            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                const shouldShow = text.includes(searchTerm.toLowerCase());
                
                row.style.display = shouldShow ? '' : 'none';
                if (shouldShow) visibleRows++;
            });

            // Mostrar/ocultar mensaje de "sin resultados"
            if (visibleRows === 0 && searchTerm.trim() !== '') {
                noResults.classList.remove('d-none');
                tableBody.closest('.table-responsive').style.display = 'none';
            } else {
                noResults.classList.add('d-none');
                tableBody.closest('.table-responsive').style.display = 'block';
            }

            // Actualizar contador de resultados
            document.getElementById('resultadosBusqueda').textContent = visibleRows;
        }

        // Limpiar búsqueda
        function clearSearch() {
            document.getElementById('searchInput').value = '';
            searchDocentes('');
        }

        // Guardar docente
        function saveDocente() {
            const form = document.getElementById('addDocenteForm');
            const formData = new FormData(form);
            
            // Validación básica
            if (!formData.get('dni') || !formData.get('primer_apellido') || !formData.get('segundo_apellido') ||
                !formData.get('primer_nombre') || !formData.get('correo_institucional') || 
                !formData.get('celular') ) {
                alert('Por favor completa todos los campos obligatorios');
                return;
            }

            // Enviar formulario
            form.submit();
        }

        // Editar docente
        function editDocente(id) {
            // Redirigir a la página de edición
            window.location.href = `/docentes/editar/${id}/`;
        }

        // Confirmar eliminación
        function confirmDelete(id, name) {
            currentDocenteId = id;
            document.getElementById('docenteToDelete').textContent = name;
            
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.show();
            
            // Configurar botón de confirmación
            document.getElementById('confirmDeleteBtn').onclick = function() {
                deleteDocente(id);
            };
        }

        // Eliminar docente
        function deleteDocente(id) {
            // Crear formulario para envío POST/DELETE
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/docentes/eliminar/${id}/`;
            
            // Agregar token CSRF
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
            if (csrfToken) {
                const csrfInput = document.createElement('input');
                csrfInput.type = 'hidden';
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = csrfToken.value;
                form.appendChild(csrfInput);
            }
            
            document.body.appendChild(form);
            form.submit();
        }

                    // Validación de DNI en tiempo real
                    document.addEventListener('input', function(e) {
                        if (e.target.name === 'dni') {
                            e.target.value = e.target.value.replace(/[^0-9]/g, '').substring(0, 8);
                        }
                    });

    function loadEditData(id, nombre,nombre2, apellido, apellido2, correo, celular) {
                // Llenar inputs
                document.getElementById('editId').value = id;
                document.getElementById('editNombre').value = nombre;
                document.getElementById('editNombre2').value = nombre2;
                document.getElementById('editApellido').value = apellido;
                document.getElementById('editApellido2').value = apellido2;
                document.getElementById('editCorreo').value = correo;
                document.getElementById('editCelular').value = celular;

                // Cambiar acción del form dinámicamente
                document.getElementById('editDocenteForm').action = "/docentes/editar/" + id;
            }