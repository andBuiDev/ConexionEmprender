from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

emprendimientos = [
   # Construcción
    {"id": 1, "nombre": "Albañil Sabaneta", "descripcion": "Servicios de construcción profesionales.", "imagen": "Albañil.jpg", "categoria": "Construcción"},
    {"id": 2, "nombre": "Electricista Total", "descripcion": "Instalaciones eléctricas seguras.", "imagen": "electricista.jpg", "categoria": "Construcción"},
    {"id": 3, "nombre": "Diseño de Interiores", "descripcion": "Remodelamos tus espacios con estilo.", "imagen": "interiores.jpg", "categoria": "Construcción"},
    {"id": 21, "nombre": "Albañil Sabaneta", "descripcion": "Servicios de construcción profesionales.", "imagen": "Albañil.jpg", "categoria": "Construcción"},
    {"id": 22, "nombre": "Electricista Total", "descripcion": "Instalaciones eléctricas seguras.", "imagen": "electricista.jpg", "categoria": "Construcción"},
    {"id": 23, "nombre": "Diseño de Interiores", "descripcion": "Remodelamos tus espacios con estilo.", "imagen": "interiores.jpg", "categoria": "Construcción"},
    {"id": 24, "nombre": "Construcciones caldecast", "descripcion": "Construcción, remodelaciones, ampliaciones, reparaciones.", "imagen": "electricista.jpg", "categoria": "Construcción"},
    {"id": 25, "nombre": "Javier mira", "descripcion": "Todo en construcción y reformas.", "imagen": "electricista.jpg", "categoria": "Construcción"},
    {"id": 26, "nombre": "Jhon jaramillo", "descripcion": "Soluciones eléctricas integradas para residencias y comercios.", "imagen": "electricista.jpg", "categoria": "Construcción"},
    {"id": 27, "nombre": "Denny angulo", "descripcion": "Servicios eléctricos, pintura, paneles solares.", "imagen": "electricista.jpg", "categoria": "Construcción"},

    # Alimentos
    {"id": 4, "nombre": "Café de la Montaña", "descripcion": "Café orgánico de altura.", "imagen": "Cafe de especialidad.jpg", "categoria": "Alimentos"},
    {"id": 5, "nombre": "Panadería Doña Rosa", "descripcion": "Pan artesanal recién horneado.", "imagen": "panaderia.jpg", "categoria": "Alimentos"},
    {"id": 6, "nombre": "Miel Pura", "descripcion": "Miel natural de abejas sin químicos.", "imagen": "miel.jpg", "categoria": "Alimentos"},
    {"id": 28, "nombre": "Café marquesina", "descripcion": "Café de calidad.", "imagen": "cafe.jpg", "categoria": "Alimentos"},
    {"id": 29, "nombre": "Donde la abuela", "descripcion": "Sopa de sancocho, frijoles y otros platos tradicionales.", "imagen": "comida.jpg", "categoria": "Alimentos"},
    {"id": 30, "nombre": "El mana", "descripcion": "Arepas de queso.", "imagen": "arepas.jpg", "categoria": "Alimentos"},
    {"id": 31, "nombre": "Los tamales de la abuela", "descripcion": "Tamales gourmet.", "imagen": "tamales.jpg", "categoria": "Alimentos"},
    {"id": 32, "nombre": "Super perritos", "descripcion": "Hamburguesas, chuzos, perros calientes, combos.", "imagen": "comidarapida.jpg", "categoria": "Alimentos"},
    {"id": 33, "nombre": "Miche pizza", "descripcion": "Pizzas artesanales.", "imagen": "pizza.jpg", "categoria": "Alimentos"},
    {"id": 34, "nombre": "Pollo campesino", "descripcion": "Pollo directo de la finca sin químicos.", "imagen": "pollo.jpg", "categoria": "Alimentos"},
    {"id": 35, "nombre": "Dulce morr", "descripcion": "Helados, dulces, malteadas, fresas, vino, café saludable.", "imagen": "postres.jpg", "categoria": "Alimentos"},

    # Belleza
    {"id": 7, "nombre": "Belleza Natural", "descripcion": "Cosméticos veganos y cruelty-free.", "imagen": "belleza.jpg", "categoria": "Belleza"},
    {"id": 8, "nombre": "Barbería Clásica", "descripcion": "Cortes de cabello y barba con tradición.", "imagen": "barberia.jpg", "categoria": "Belleza"},
    {"id": 36, "nombre": "Omorfia cosmética natural", "descripcion": "Productos cosméticos para tratamiento capilar.", "imagen": "cosmetica.jpg", "categoria": "Belleza"},
    {"id": 37, "nombre": "Cejas y pestañas", "descripcion": "Tratamiento para cejas y uñas.", "imagen": "cejas.jpg", "categoria": "Belleza"},
    {"id": 38, "nombre": "Manuela sanchez", "descripcion": "Servicios de belleza y cuidado personal.", "imagen": "belleza2.jpg", "categoria": "Belleza"},
    {"id": 39, "nombre": "Liliana caro", "descripcion": "Servicios de keratina orgánica y cepillado a domicilio.", "imagen": "keratina.jpg", "categoria": "Belleza"},

    # Tecnología
    {"id": 13, "nombre": "Reparación de Celulares", "descripcion": "Soluciones rápidas y garantizadas.", "imagen": "celulares.jpg", "categoria": "Tecnología"},
    {"id": 14, "nombre": "Diseño Web", "descripcion": "Creamos tu página web profesional.", "imagen": "disenoweb.jpg", "categoria": "Tecnología"},
    {"id": 40, "nombre": "Arreglos Cristian castano", "descripcion": "Servicio técnico a domicilio para computadoras, instalación de programas.", "imagen": "computadoras.jpg", "categoria": "Tecnología"},
    {"id": 41, "nombre": "Tecno soluciones", "descripcion": "Servicio técnico para computadoras, venta de accesorios.", "imagen": "tecnologia.jpg", "categoria": "Tecnología"},
    {"id": 42, "nombre": "Electro todo", "descripcion": "Reparación y mantenimiento de electrodomésticos.", "imagen": "electrodomesticos.jpg", "categoria": "Tecnología"},
    {"id": 43, "nombre": "Servicio técnico a domicilio", "descripcion": "Mantenimiento de refrigeradoras y lavadoras.", "imagen": "lavadoras.jpg", "categoria": "Tecnología"},

    # Hogar
    {"id": 17, "nombre": "Muebles Rústicos", "descripcion": "Muebles con madera reciclada.", "imagen": "muebles.jpg", "categoria": "Hogar"},
    {"id": 18, "nombre": "Plantas de Interior", "descripcion": "Plantas que purifican tu hogar.", "imagen": "plantas.jpg", "categoria": "Hogar"},
    {"id": 44, "nombre": "Jc muebles", "descripcion": "Venta de camas ideales para cada necesidad.", "imagen": "muebles2.jpg", "categoria": "Hogar"},
    {"id": 45, "nombre": "Variedades jotic", "descripcion": "Percheros de madera, diseño funcional y elegante para hogar u oficina.", "imagen": "percheros.jpg", "categoria": "Hogar"},
    {"id": 46, "nombre": "Paola Andrea", "descripcion": "Vajillas corona aptas para microondas.", "imagen": "vajillas.jpg", "categoria": "Hogar"},
    {"id": 47, "nombre": "Tapiz lavados", "descripcion": "Lavado profesional de muebles.", "imagen": "tapizados.jpg", "categoria": "Hogar"},
    {"id": 48, "nombre": "Max limp c.b", "descripcion": "Lavado y desinfección de muebles, colchones, cortinas, alfombras.", "imagen": "limpieza.jpg", "categoria": "Hogar"},

    # Servicios
    {"id": 49, "nombre": "Lavados rueda", "descripcion": "Lavado de muebles y colchones, eliminación de ácaros y chinches.", "imagen": "lavado.jpg", "categoria": "Servicios"},
    {"id": 50, "nombre": "Jorge gallego", "descripcion": "Destaqueo de tuberías sin romper, limpieza de lavaplatos, patios, baños, sanitarios.", "imagen": "plomeria.jpg", "categoria": "Servicios"},
    {"id": 51, "nombre": "Jaime destaqueador", "descripcion": "Destape de tuberías sin romper pisos.", "imagen": "destape.jpg", "categoria": "Servicios"},
    {"id": 52, "nombre": "Juan martinez", "descripcion": "Destape de cañerías atascadas sin romper.", "imagen": "plomeria2.jpg", "categoria": "Servicios"},
    {"id": 53, "nombre": "Lisa Millán", "descripcion": "Servicio de limpieza de hogar.", "imagen": "limpieza2.jpg", "categoria": "Servicios"},
    {"id": 54, "nombre": "@alquilolavadoras", "descripcion": "Alquiler de lavadoras digitales y de doble tina.", "imagen": "lavadoras2.jpg", "categoria": "Servicios"},
    {"id": 55, "nombre": "Salud para dos", "descripcion": "Atención domiciliaria por médico y odontólogo.", "imagen": "medico.jpg", "categoria": "Servicios"},
    {"id": 56, "nombre": "Instalamos seguridad", "descripcion": "Instalación y mantenimiento de sistemas de seguridad para propiedades.", "imagen": "seguridad.jpg", "categoria": "Servicios"},
    {"id": 57, "nombre": "Seguridad industrial", "descripcion": "Extintores ABC para hogares y empresas.", "imagen": "extintores.jpg", "categoria": "Servicios"},
    {"id": 58, "nombre": "Vanne PB", "descripcion": "Servicio de soldadura eléctrica a domicilio.", "imagen": "soldadura.jpg", "categoria": "Servicios"},

    # Moda
    {"id": 15, "nombre": "Ropa Ecológica", "descripcion": "Prendas sostenibles y cómodas.", "imagen": "ropa.jpg", "categoria": "Moda"},
    {"id": 16, "nombre": "Zapatos Hechos a Mano", "descripcion": "Calzado artesanal duradero.", "imagen": "zapatos.jpg", "categoria": "Moda"},
    {"id": 59, "nombre": "Tienda v azul", "descripcion": "Ropa deportiva para dama y caballero, accesorios fitness.", "imagen": "deportiva.jpg", "categoria": "Moda"},
    {"id": 60, "nombre": "El ropero magico", "descripcion": "Venta de ropa de segunda mano.", "imagen": "ropausada.jpg", "categoria": "Moda"},
    {"id": 61, "nombre": "Monica munoz", "descripcion": "Venta de camisetas desde $10.500.", "imagen": "camisetas.jpg", "categoria": "Moda"},
    {"id": 62, "nombre": "Pijamas lizz", "descripcion": "Pijamas de piel de durazno.", "imagen": "pijamas.jpg", "categoria": "Moda"},
    {"id": 63, "nombre": "Santiago gomez", "descripcion": "Venta de prendas para niñas desde $10.000.", "imagen": "ninas.jpg", "categoria": "Moda"},

    # Eventos
    {"id": 64, "nombre": "Inter foto alexander", "descripcion": "Mosaicos, filmaciones de eventos empresariales, matrimonios, bautizos.", "imagen": "fotografia.jpg", "categoria": "Eventos"},
    {"id": 65, "nombre": "Diversión", "descripcion": "Servicios para fiestas infantiles, cumpleaños.", "imagen": "fiestas.jpg", "categoria": "Eventos"},
    {"id": 66, "nombre": "Topys eventos", "descripcion": "Desayunos en topys.", "imagen": "eventos.jpg", "categoria": "Eventos"},
    {"id": 67, "nombre": "Tres mosqueteros", "descripcion": "Anchetas y más.", "imagen": "anchetas.jpg", "categoria": "Eventos"},

    # Salud
    {"id": 19, "nombre": "Masajes Relajantes", "descripcion": "Terapias para aliviar el estrés.", "imagen": "masajes.jpg", "categoria": "Salud"},
    {"id": 20, "nombre": "Yoga en Casa", "descripcion": "Clases virtuales para todos los niveles.", "imagen": "yoga.jpg", "categoria": "Salud"},
    {"id": 68, "nombre": "Divi her envigado", "descripcion": "Desintoxicación por 7 días, eliminación de parásitos.", "imagen": "desintoxicacion.jpg", "categoria": "Salud"},
    {"id": 69, "nombre": "Omega", "descripcion": "Club de gimnasia y porrismo.", "imagen": "gimnasia.jpg", "categoria": "Salud"},
    {"id": 70, "nombre": "Carlos Jaramillo", "descripcion": "Entrenador personal profesional.", "imagen": "entrenador.jpg", "categoria": "Salud"},
    {"id": 71, "nombre": "Encantos Rosana", "descripcion": "Cojín para glúteos, recuperación y tratamiento.", "imagen": "gluteos.jpg", "categoria": "Salud"},

    # Varios
    {"id": 72, "nombre": "The best shop", "descripcion": "Videojuegos y más.", "imagen": "videojuegos.jpg", "categoria": "Varios"},
    {"id": 73, "nombre": "Don martin", "descripcion": "Palitos de queso con salsa de mora.", "imagen": "palitos.jpg", "categoria": "Varios"},
    {"id": 74, "nombre": "Vinos don martin", "descripcion": "Vinos de calidad.", "imagen": "vinos.jpg", "categoria": "Varios"},
    {"id": 75, "nombre": "Perfumes", "descripcion": "Venta de splash de Victoria's Secret originales.", "imagen": "perfumes.jpg", "categoria": "Varios"},
    {"id": 76, "nombre": "Crema multiusos", "descripcion": "Crema limpiadora multiusos.", "imagen": "crema.jpg", "categoria": "Varios"},
    {"id": 77, "nombre": "Jasmin alzate", "descripcion": "Productos americanos con factura.", "imagen": "importados.jpg", "categoria": "Varios"},
    {"id": 78, "nombre": "La despensa paisa", "descripcion": "Productos frescos del campo (huevos, cuajada, quesos, arepas).", "imagen": "despensa.jpg", "categoria": "Varios"},
    {"id": 79, "nombre": "Bar requintadero", "descripcion": "Alcohol, cerveza, bebidas fuertes y comidas.", "imagen": "bar.jpg", "categoria": "Varios"},
    {"id": 80, "nombre": "En línea blanca", "descripcion": "Servicio técnico a aparatos electrodomésticos.", "imagen": "lineablanca.jpg", "categoria": "Varios"}
]

@app.route('/')
def home():
    categorias = sorted({emp["categoria"] for emp in emprendimientos})
    return render_template('index.html', 
                         emprendimientos=emprendimientos,
                         categorias=categorias,
                         obtenerIconoCategoria=obtenerIconoCategoria)

@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    print(f"Producto añadido al carrito: {data['product_id']}")
    return jsonify({"status": "success"})

@app.route('/registro')
def mostrar_formulario_registro():
    return render_template('registroindex.html')

@app.route('/registro/exito')
def registro_exito():
    return render_template('registrolog_in.html')

def obtenerIconoCategoria(categoria):
    iconos = {
        "Construcción": "hammer",
        "Alimentos": "utensils",
        "Belleza": "spa",
        "Educación": "graduation-cap",
        "Artesanías": "palette",
        "Tecnología": "laptop-code",
        "Moda": "tshirt",
        "Hogar": "home",
        "Salud": "heartbeat"
    }
    return iconos.get(categoria, "tag")

if __name__ == '__main__':
    app.run(debug=True)
    
    