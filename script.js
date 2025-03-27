document.addEventListener("DOMContentLoaded", async function () {
    try {
        const listaHistorias = document.getElementById("lista-historias");
        const contenedorPrincipal = document.getElementById("historia-reciente");
        
        // Cargar y ordenar historias
        const archivos = await fetch("historias/lista.json").then(res => res.json());
        if (!archivos.length) return mostrarError("No hay historias disponibles");

        archivos.sort((a, b) => {
            const getTime = (str) => {
                const [year, month, day, time] = str.split(".html")[0].split("-");
                return new Date(`${year}-${month}-${day}T${time.slice(0, 2)}:${time.slice(2)}`).getTime();
            };
            return getTime(b) - getTime(a);
        });

        // Precargar metadatos
        const historiasMetadata = await Promise.all(archivos.map(async archivo => {
            const html = await fetch(`historias/${archivo}`).then(res => res.text());
            const doc = new DOMParser().parseFromString(html, "text/html");
            return {
                archivo,
                titulo: doc.querySelector("h1")?.textContent || "Sin título",
                fecha: doc.querySelector("small")?.textContent || "Fecha desconocida"
            };
        }));

        // Cargar historia principal
        const cargarContenido = async (archivo) => {
            const html = await fetch(`historias/${archivo}`).then(res => res.text());
            const doc = new DOMParser().parseFromString(html, "text/html");
            const article = doc.querySelector("article").cloneNode(true);
            article.querySelector("h1")?.remove();
            article.querySelector("small")?.remove();
            return article.innerHTML;
        };

        const actualizarVista = (titulo, fecha, contenido) => {
            document.getElementById("titulo-historia").textContent = titulo;
            document.getElementById("fecha-historia").textContent = fecha;
            document.getElementById("contenido-historia").innerHTML = contenido;
        };

        // Mostrar inicial
        const primera = historiasMetadata[0];
        actualizarVista(primera.titulo, primera.fecha, await cargarContenido(archivos[0]));

        // Generar lista dinámica
        const actualizarLista = (currentArchivo) => {
            listaHistorias.innerHTML = historiasMetadata
                .filter(m => m.archivo !== currentArchivo)
                .slice(0, 2)
                .map(m => `
                    <li>
                        <a href="#" data-archivo="${m.archivo}" class="cargar-historia">
                            ${m.titulo}
                            <small>${m.fecha}</small>
                        </a>
                    </li>
                `).join("");
        };

        actualizarLista(archivos[0]);

        // Manejador de clics
        listaHistorias.addEventListener("click", async (e) => {
            if (!e.target.closest(".cargar-historia")) return;
            e.preventDefault();
            const archivo = e.target.closest("a").dataset.archivo;
            const metadata = historiasMetadata.find(m => m.archivo === archivo);
            actualizarVista(metadata.titulo, metadata.fecha, await cargarContenido(archivo));
            contenedorPrincipal.scrollIntoView({ behavior: "smooth" });
            actualizarLista(archivo);
        });

    } catch (error) {
        console.error("Error:", error);
        mostrarError("Error cargando contenido");
    }
});

function mostrarError(mensaje) {
    const contenedor = document.createElement("div");
    contenedor.className = "error";
    contenedor.textContent = mensaje;
    document.body.prepend(contenedor);
}