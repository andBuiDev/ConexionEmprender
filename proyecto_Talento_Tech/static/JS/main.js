// Carrito de compras
let cartItems = 0;
const cartBtn = document.querySelector('.cart-btn');
const cartCount = document.querySelector('.cart-count');

cartBtn.addEventListener('click', (e) => {
    e.preventDefault();
    cartItems++;
    cartCount.textContent = cartItems;
    // API Flask
    fetch('/api/add_to_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_id: cartItems })
    });
});

// Botones "Me Interesa"
document.querySelectorAll('.interest-btn').forEach(button => {
    button.addEventListener('click', () => {
        const cardTitle = button.closest('.card').querySelector('.card-title').textContent;
        alert(`¡Gracias por tu interés en "${cardTitle}"! 🚀\nPronto te contactaremos con más información.`);
    });
});

document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        const categoria = e.target.textContent.trim();
        alert(`Filtrando por: ${categoria}`);
        // llamada a Flask para filtrar
    });
});

function buscarEmprendimientos(event) {
    event.preventDefault();
    const busqueda = document.getElementById('busquedaInput').value.toLowerCase();
    const tarjetas = document.querySelectorAll('.card');
    let categoriasConResultados = new Set();
    
    // Si la búsqueda coincide exactamente con una categoría, filtrar por ella
    const categorias = Array.from(document.querySelectorAll('#categoriesMenu .dropdown-item'))
        .map(item => item.textContent.trim().replace(/\s+\d+$/, '')); // Remueve el contador si existe
    
    if (categorias.includes(busqueda)) {
        filtrarPorCategoria(busqueda);
        return;
    }


    // Primera pasada: ocultar/mostrar tarjetas y recolectar categorías con resultados
    tarjetas.forEach(tarjeta => {
        const titulo = tarjeta.querySelector('.card-title').textContent.toLowerCase();
        const descripcion = tarjeta.querySelector('.card-text').textContent.toLowerCase();
        const categoria = tarjeta.closest('.slider-categoria').id.replace('slider-', '');
        
        if (titulo.includes(busqueda) || descripcion.includes(busqueda)) {
            tarjeta.style.display = 'block';
            categoriasConResultados.add(categoria);
        } else {
            tarjeta.style.display = 'none';
        }
    });

    // Segunda pasada: mostrar/ocultar secciones de categorías
    document.querySelectorAll('.slider-categoria').forEach(seccion => {
        const categoriaId = seccion.id.replace('slider-', '');
        const categoriaSection = seccion.closest('.position-relative'); // El contenedor de la categoría
        
        if (categoriasConResultados.has(categoriaId) || busqueda === '') {
            categoriaSection.style.display = 'block';
        } else {
            categoriaSection.style.display = 'none';
        }
    });

    // Dentro de buscarEmprendimientos, después de procesar los resultados
if (categoriasConResultados.size === 0 && busqueda !== '') {
    const noResults = document.createElement('div');
    noResults.className = 'alert alert-info text-center my-5';
    noResults.innerHTML = `<i class="fas fa-info-circle me-2"></i> No se encontraron resultados para "${busqueda}"`;
    document.querySelector('main').appendChild(noResults);
    
    // Remover el mensaje después de 5 segundos o al hacer nueva búsqueda
    setTimeout(() => noResults.remove(), 5000);
}
}

// Función para deslizar sliders
function deslizarSlider(categoria, direccion) {
    const slider = document.getElementById(`slider-${categoria}`);
    const inner = slider.querySelector('.slider-inner');
    const items = inner.querySelectorAll('.slider-item');
    
    if (items.length === 0) return; // Si no hay items, salir
    
    // Calcular el ancho de un item 
    const itemWidth = items[0].offsetWidth + 
                     parseInt(window.getComputedStyle(items[0]).marginRight);
    
    // Calcular cuántos items caben en el contenedor
    const visibleItems = Math.floor(slider.offsetWidth / itemWidth);
    
    // Calcular el desplazamiento (1 item o el número visible)
    const scrollAmount = itemWidth * (direccion > 0 ? visibleItems : -visibleItems);
    
    // Aplicar el desplazamiento con animación suave
    inner.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
    });
    
        function actualizarFlechas(categoria) {
    const slider = document.getElementById(`slider-${categoria}`);
    const inner = slider.querySelector('.slider-inner');
    const leftArrow = slider.previousElementSibling;
    const rightArrow = slider.nextElementSibling;
    
    leftArrow.style.visibility = inner.scrollLeft <= 0 ? 'hidden' : 'visible';
    rightArrow.style.visibility = inner.scrollLeft + inner.clientWidth >= inner.scrollWidth ? 'hidden' : 'visible';
    }
    inner.addEventListener('scroll', () => actualizarFlechas(categoria));
    
    document.querySelectorAll('.slider-container').forEach(container => {
    const categoria = container.id.replace('slider-', '');
    actualizarFlechas(categoria);
});
}


function resetearBusqueda() {
    document.getElementById('busquedaInput').value = '';
    
    // Mostrar todas las tarjetas
    document.querySelectorAll('.card').forEach(tarjeta => {
        tarjeta.style.display = 'block';
    });
    
    // Mostrar todas las categorías
    document.querySelectorAll('.position-relative').forEach(seccion => {
        seccion.style.display = 'block';
    });
}

// Función para filtrar por categoría
function filtrarPorCategoria(categoria) {
    // Ocultar todas las secciones primero
    document.querySelectorAll('.position-relative').forEach(seccion => {
        seccion.style.display = 'none';
    });
    
    // Mostrar solo la categoría seleccionada
    const seccionesCategoria = document.querySelectorAll(`.badge.bg-orange`);
    seccionesCategoria.forEach(badge => {
        if (badge.textContent === categoria) {
            const seccion = badge.closest('.position-relative');
            seccion.style.display = 'block';
            seccion.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
    
    // Actualizar el input de búsqueda
    document.getElementById('busquedaInput').value = categoria;
    
    // Cambiar el texto del botón de categorías
    document.getElementById('categoriesDropdown').innerHTML = 
        `<i class="fas fa-list me-2"></i>${categoria}`;
}

// Función para mostrar todos los emprendimientos
function mostrarTodos() {
    document.querySelectorAll('.position-relative').forEach(seccion => {
        seccion.style.display = 'block';
    });
    
    // Mostrar todas las tarjetas
    document.querySelectorAll('.card').forEach(tarjeta => {
        tarjeta.style.display = 'block';
    });
    
    // Resetear el input de búsqueda
    document.getElementById('busquedaInput').value = '';
    
    // Restaurar el texto del botón de categorías
    document.getElementById('categoriesDropdown').innerHTML = 
        `<i class="fas fa-list me-2"></i>Categorías`;
    
    // Desplazarse al inicio
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// "cajita" para guardar los productos
let productosEnCarrito = [];

// carrito y el numerito
const botonCarrito = document.querySelector('.cart-btn');
const contadorCarrito = document.querySelector('.cart-count');

// Función para actualizar el numerito
function actualizarCarrito() {
    contadorCarrito.textContent = productosEnCarrito.length;
}

// clic en "Me interesa"
document.querySelectorAll('.interest-btn').forEach(boton => {
    boton.addEventListener('click', (e) => {
        e.preventDefault();
        const tarjeta = e.target.closest('.card');
        const nombreProducto = tarjeta.querySelector('.card-title').textContent;
        
        // Añadimos el producto a la "cajita"
        productosEnCarrito.push(nombreProducto);
        actualizarCarrito();
        
        // Mensaje bonito (opcional)
        alert(`¡Añadiste "${nombreProducto}" al carrito! 🎉`);
    });
});

// clic en el icono del carrito
botonCarrito.addEventListener('click', (e) => {
    e.preventDefault();
    if (productosEnCarrito.length === 0) {
        alert("El carrito está vacío. ¡Añade algo primero! 😊");
    } else {
        alert(`Tienes estos productos:\n${productosEnCarrito.join('\n')}`);
    }
});

// Botón de Registro - Alert con enlace
document.querySelectorAll('a[href*="/registro"]').forEach(boton => {
    boton.addEventListener('click', (e) => {
        e.preventDefault(); // Detenemos el comportamiento normal
        const urlRegistro = boton.getAttribute('href'); // Obtenemos el link
        
        // Alert personalizado
        if(confirm(`¿Quieres registrarte? 🌟\n\nPuedes hacerlo aquí:\n${urlRegistro}\n\n¿Abrir ahora?`)) {
            window.location.href = urlRegistro; // Redirigimos si dice "Sí"
        }
    });
});