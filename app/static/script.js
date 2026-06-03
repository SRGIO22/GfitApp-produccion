/* ============================================
   Menú hamburguesa: cerrar al hacer clic en un enlace
   ============================================ */
document.addEventListener("click", function(e) {
    const toggle = document.getElementById("menu-toggle");
    if (!toggle) return;
    const link = e.target.closest(".nav-menu-link");
    if (link && toggle.checked) {
        toggle.checked = false;
    }
});

/* ============================================
   Mostrar / ocultar spinner de carga
   ============================================ */
function mostrarSpinner(contenedor) {
    if (!contenedor) return;
    contenedor.innerHTML = '<div class="spinner"><span>Cargando...</span></div>';
}

/* ============================================
   Funciones para el listado de clases
   ============================================ */
function pintarClases(lista) {
    const contenedor = document.getElementById("lista-cursos");
    if (!contenedor) return;
    contenedor.innerHTML = "";
    if (!lista || lista.length === 0) {
        contenedor.innerHTML = `
            <div class="burbuja text-center">
                <h4>No hay clases disponibles</h4>
                <p>Por el momento no hay clases programadas. Vuelve a intentarlo más tarde.</p>
            </div>
        `;
        return;
    }
    lista.forEach(clase => {
        const tarjeta = `
            <div class="card mb-3 shadow-sm p-3">
                <h4>${clase.nombre_clase}</h4>
                <p>${clase.descripcion_clase}</p>
                <p>
                    <i class="bi bi-calendar-event"></i> ${clase.fecha_clase}<br>
                    <i class="bi bi-clock"></i> ${clase.hora_clase}<br>
                    <i class="bi bi-hourglass-split"></i> ${clase.duracion_clase} min<br>
                    <i class="bi bi-people"></i> Capacidad: ${clase.capacidad_max}
                </p>
                <p>
                    <i class="bi bi-person-badge"></i>
                    Entrenador: ${clase.entrenador.nombre_entrenador} ${clase.entrenador.apellidos_entrenador}
                </p>
            </div>
        `;
        contenedor.innerHTML += tarjeta;
    });
}

/* ============================================
   Cargar clases en el select de reservas
   ============================================ */
function cargarClasesEnSelect(lista) {
    const select = document.getElementById("clase");
    if (!select) return;
    window.listaClases = lista || [];
    select.innerHTML = '<option value="">Selecciona una clase</option>';
    lista.forEach(clase => {
        const opcion = document.createElement("option");
        opcion.value = clase.id_clase;
        opcion.textContent = clase.nombre_clase;
        select.appendChild(opcion);
    });
}

/* ============================================
   Mostrar detalles de la clase seleccionada
   ============================================ */
const selectClase = document.getElementById("clase");
if (selectClase) {
    selectClase.addEventListener("change", function() {
        const claseSeleccionada = (window.listaClases || []).find(c => c.id_clase == this.value);
        const info = document.getElementById("infoClase");
        if (claseSeleccionada) {
            document.getElementById("infoFecha").textContent = claseSeleccionada.fecha_clase;
            document.getElementById("infoHora").textContent = claseSeleccionada.hora_clase;
            document.getElementById("infoDuracion").textContent = claseSeleccionada.duracion_clase;
            document.getElementById("infoEntrenador").textContent =
                `${claseSeleccionada.entrenador.nombre_entrenador} ${claseSeleccionada.entrenador.apellidos_entrenador}`;
            info.classList.remove("d-none");
        } else {
            info.classList.add("d-none");
        }
    });
}

/* ============================================
   Botón "Actualizar cursos" en clases.html
   ============================================ */
document.addEventListener("DOMContentLoaded", function() {
    const btnCursos = document.getElementById("btnCursos");
    if (btnCursos) {
        btnCursos.addEventListener("click", function() {
            const contenedor = document.getElementById("lista-cursos");
            mostrarSpinner(contenedor);
            // Aquí se haría la llamada a la API para obtener las clases
            // fetch("/api/clases")
            //   .then(r => r.json())
            //   .then(data => pintarClases(data))
            //   .catch(err => { ... });
        });
    }
});

/* ============================================
   Validación del formulario de reserva con feedback visual
   ============================================ */
const form = document.getElementById("formReserva");
if (form) {
    const feedback = document.getElementById("formFeedback");
    const successMsg = document.getElementById("formSuccess");

    function mostrarError(mensaje) {
        if (!feedback) return;
        feedback.textContent = mensaje;
        feedback.style.display = "block";
        if (successMsg) successMsg.style.display = "none";
    }

    function mostrarExito(mensaje) {
        if (!successMsg) return;
        successMsg.textContent = mensaje;
        successMsg.style.display = "block";
        if (feedback) feedback.style.display = "none";
    }

    function ocultarMensajes() {
        if (feedback) feedback.style.display = "none";
        if (successMsg) successMsg.style.display = "none";
    }

    form.addEventListener("submit", function(e) {
        ocultarMensajes();
        const clase = document.getElementById("clase").value;
        if (!clase) {
            mostrarError("Por favor selecciona una clase antes de confirmar la reserva.");
            e.preventDefault();
            return;
        }
        // Simulación de envío exitoso (cuando la API esté lista, se reemplazará)
        // e.preventDefault();
        // mostrarExito("¡Reserva confirmada con éxito!");
    });

    form.addEventListener("reset", function() {
        ocultarMensajes();
        const info = document.getElementById("infoClase");
        if (info) info.classList.add("d-none");
    });
}

/* ============================================
   Perfil de usuario — vista y edición
   ============================================ */
document.addEventListener("DOMContentLoaded", function() {
    const vista = document.getElementById("perfilVista");
    const edicion = document.getElementById("perfilEdicion");
    if (!vista) return;

    const datosGuardados = JSON.parse(localStorage.getItem("gfitapp_perfil"));

    const demo = {
        nombre: "Ángel",
        apellidos: "Albarracín",
        email: "angel@example.com",
        telefono: "612 345 678"
    };

    const usuario = datosGuardados || demo;

    function ocultarFeedback() {
        ["perfilSuccess", "perfilFeedback"].forEach(function(id) {
            const el = document.getElementById(id);
            if (el) el.style.display = "none";
        });
    }

    function mostrarVista() {
        document.getElementById("vistaNombre").textContent = usuario.nombre;
        document.getElementById("vistaApellidos").textContent = usuario.apellidos;
        document.getElementById("vistaEmail").textContent = usuario.email;
        document.getElementById("vistaTelefono").textContent = usuario.telefono;
        vista.style.display = "block";
        edicion.style.display = "none";
        ocultarFeedback();
    }

    function mostrarEdicion() {
        document.getElementById("editNombre").value = usuario.nombre;
        document.getElementById("editApellidos").value = usuario.apellidos;
        document.getElementById("editEmail").value = usuario.email;
        document.getElementById("editTelefono").value = usuario.telefono;
        vista.style.display = "none";
        edicion.style.display = "block";
        ocultarFeedback();
    }

    document.getElementById("btnEditar").addEventListener("click", mostrarEdicion);
    document.getElementById("btnCancelar").addEventListener("click", mostrarVista);

    document.getElementById("formPerfil").addEventListener("submit", function(e) {
        e.preventDefault();
        ocultarFeedback();
        usuario.nombre = document.getElementById("editNombre").value.trim();
        usuario.apellidos = document.getElementById("editApellidos").value.trim();
        usuario.email = document.getElementById("editEmail").value.trim();
        usuario.telefono = document.getElementById("editTelefono").value.trim();
        localStorage.setItem("gfitapp_perfil", JSON.stringify(usuario));
        mostrarVista();
        const success = document.getElementById("perfilSuccess");
        success.textContent = "Datos guardados correctamente.";
        success.style.display = "block";
        setTimeout(function() { success.style.display = "none"; }, 3000);
    });

    mostrarVista();
});

/* ============================================
   Panel de socio
   ============================================ */
document.addEventListener("DOMContentLoaded", function() {
    if (!document.getElementById("panelNombre")) return;

    const perfil = JSON.parse(localStorage.getItem("gfitapp_perfil")) || {
        nombre: "Ángel",
        apellidos: "Albarracín",
        email: "angel@example.com",
        telefono: "612 345 678"
    };

    document.getElementById("panelNombre").textContent = perfil.nombre || "Socio";
    document.getElementById("panelEmail").textContent = perfil.email || "—";
    document.getElementById("panelTelefono").textContent = perfil.telefono || "—";

    const reservas = JSON.parse(localStorage.getItem("gfitapp_reservas")) || [];
    const count = reservas.length;
    document.getElementById("panelResumenHistorial").textContent =
        count > 0 ? count + " reserva" + (count > 1 ? "s" : "") + " realizada" + (count > 1 ? "s" : "") : "Aún sin reservas";

    const meta = 12;
    document.getElementById("progresoClases").textContent = count;
    document.getElementById("progresoMeta").textContent = count + " / " + meta;
    var pct = Math.min(100, Math.round((count / meta) * 100));
    document.getElementById("barraProgreso").style.width = pct + "%";
    document.getElementById("barraMeta").style.width = pct + "%";
});

/* ============================================
   Mostrar historial de reservas
   ============================================ */
function pintarHistorial(lista) {
    const contenedor = document.getElementById("lista-historial");
    if (!contenedor) return;
    contenedor.innerHTML = "";
    if (!lista || lista.length === 0) {
        contenedor.innerHTML = `
            <div class="burbuja text-center">
                <h4>No tienes reservas registradas.</h4>
                <p>Cuando reserves una clase, aparecerá aquí.</p>
            </div>
        `;
        return;
    }
    lista.forEach(reserva => {
        const tarjeta = `
            <div class="card mb-3 shadow-sm p-3">
                <h4>${reserva.clase.nombre_clase}</h4>
                <p>
                    <i class="bi bi-calendar-event"></i> ${reserva.clase.fecha_clase}<br>
                    <i class="bi bi-clock"></i> ${reserva.clase.hora_clase}<br>
                    <i class="bi bi-hourglass-split"></i> ${reserva.clase.duracion_clase} min
                </p>
                <p>
                    <i class="bi bi-person-badge"></i>
                    Entrenador: ${reserva.clase.entrenador.nombre_entrenador} 
                    ${reserva.clase.entrenador.apellidos_entrenador}
                </p>
                <p>
                    <i class="bi bi-check2-circle"></i>
                    Reserva realizada el: ${reserva.fecha_reserva}
                </p>
            </div>
        `;
        contenedor.innerHTML += tarjeta;
    });
}