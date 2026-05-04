from flask import Flask, render_template, abort

app = Flask(__name__)

# Secciones de la tienda
colecciones = [
    {"id": "aceites", "nombre": "Aceites Motor", "img": "Coleccion Aceite.png", "desc": "Máxima vida para tu motor con calidad Premium."},
    {"id": "grasas", "nombre": "Grasas Pro", "img": "Coleccion Grasa.png", "desc": "Lubricación extrema para rodamientos y piezas."},
    {"id": "octane", "nombre": "Aditivos", "img": "Octane.png", "desc": "Potencia extra y limpieza de inyectores."}
]

# Inventario basado en tu collage
productos = [
    {"id": 1, "col_id": "aceites", "nombre": "Aceite SAE 10W-40", "precio": "$8500", "img": "Aceite SAE 10W-40.png", "detalle": """Aceite Sintético Multiuso Motisi SAE 10W-40, un lubricante diseñado para motores de gasolina y diésel. Se comercializa principalmente en Cuba (específicamente en regiones como La Habana y Marianao) en un formato de 5 litros. [1, 2, 3, 4]

Detalles del producto

Viscosidad: SAE 10W-40, lo que indica un buen desempeño tanto en arranques en frío como en temperaturas de operación calientes.

Compatibilidad: Apto para motores de gasolina y diésel. Algunas especificaciones encontradas en productos similares de la marca mencionan clasificaciones API SL/CF o CI-4/SL.

Beneficios promocionados: La publicidad resalta una protección total, mayor eficiencia y un arranque en frío óptimo.

"""},
    {"id": 2, "col_id": "aceites", "nombre": "Aceite SAE 15W-40", "precio": "$13500cup", "img": "Aceite SAE 15W-40.png", "detalle": """Aceite Sintético Multiuso MOTISI SAE 15W-40, un lubricante diseñado para motores de gasoil y gasolina. Este aceite utiliza 'Tecnología Japonesa' y cumple con las especificaciones API:CI-4/SL, lo que lo hace adecuado tanto para motores diésel de servicio pesado como para motores de gasolina de alto rendimiento. 

Características Principales del Aceite MOTISI 15W-40:

Viscosidad Multigrado (15W-40): Proporciona fluidez y protección durante el arranque en frío (grado 15W) y mantiene una viscosidad robusta para proteger los componentes a temperaturas de operación normales (grado 40).

Base Sintética: A diferencia de los aceites minerales convencionales, su formulación sintética ofrece una mayor resistencia a la oxidación, mejor limpieza del motor y protección contra el desgaste en condiciones extremas.

Compatibilidad Dual: Está formulado para manejar los altos niveles de hollín y subproductos de combustión típicos de los motores diésel, mientras proporciona la fluidez necesaria para motores de gasolina.

Presentación: Se comercializa comúnmente en envases sellados de 5 litros."""},
    {"id": 3, "col_id": "aceites", "nombre": "Aceite SAE 20W-50", "precio": "$8500", "img": "Aceite SAE 20W-40.png", "detalle": """Aceite Motisi Sintético Multiuso SAE 20W-50, un lubricante diseñado para motores de gasolina y gasoil que ofrece una viscosidad adecuada para climas cálidos o motores con mayor kilometraje. 

Detalles del Producto

Viscosidad (SAE 20W-50): El '20W' indica su fluidez en frío, siendo apto para arranques hasta aproximadamente -15 °C. El '50' indica que mantiene una película de lubricación gruesa a altas temperaturas operativas, lo cual es ideal para evitar el desgaste bajo cargas pesadas o calor extremo.

Certificaciones (API CI-4/SL): Cumple con estándares de rendimiento para motores diésel de servicio pesado (CI-4) y motores de gasolina fabricados hasta el año 2004 (SL).

Formato: Comúnmente comercializado en envases de 5 litros.

Usos Recomendados: Es una opción versátil para automóviles, camionetas, motocicletas de 4 tiempos y equipo pesado.
"""},
    {"id": 4, "col_id": "grasas", "nombre": "Grasa Basada en Litio", "precio": "$5000cup", "img": "Grasa de Litio.png", "detalle": """ Grasa de Litio MOTISI, un lubricante diseñado para maquinaria pesada en sectores como la agricultura y la construcción. Sin embargo, la imagen publicitaria compartida ha sido generada o modificada mediante inteligencia artificial, tal como indican las huellas digitales detectadas en el archivo.

La grasa Motisi es una grasa industrial de base litio de alto rendimiento que ofrece diversas ventajas para el mantenimiento de equipos:

Protección y Durabilidad: Está formulada para proteger contra la corrosión y la oxidación, ofreciendo una lubricación fuerte para trabajos pesados.

Resistencia: Es resistente al agua y a la humedad, lo que la hace ideal para equipos que operan en exteriores o condiciones difíciles.

Reducción de Desgaste: Ayuda a reducir el desgaste y la fricción en componentes críticos como rodamientos y ejes.

Aplicaciones Comunes: Se recomienda para excavadoras, cargadores frontales, tractores agrícolas, grúas y maquinaria industrial en general."""},
        {"id": 5, "col_id": "grasas", "nombre": "Grasa Azul Multiuso", "precio": "$5000cup", "img": "Grasa Azul Multiuso.png", "detalle": """Motisi Blue Multiuse Solid Grease. Esta es una grasa lubricante que utiliza una fórmula a base de litio, diseñada para aplicaciones que requieren resistencia a altas temperaturas y presiones extremas.

Aunque la publicidad menciona 'Tecnología Japonesa', los anuncios clasificados indican que es una marca comúnmente comercializada en Cuba, especialmente en La Habana. La imagen en sí misma muestra indicios de haber sido generada o modificada mediante inteligencia artificial (como se detectó mediante análisis de huellas digitales digitales).

Características Principales

Esta grasa, identificada frecuentemente como EP2, ofrece las siguientes propiedades:

Multiuso: Apta para rodamientos de alta temperatura, chasis de vehículos, maquinaria agrícola y equipo industrial pesado.

Resistencia: Formulada para soportar el lavado por agua, la corrosión y la oxidación.

Consistencia: Al ser una grasa de litio azul, suele tener una textura suave pero pegajosa que garantiza que el lubricante permanezca en su lugar bajo cargas pesadas."""
    {"id": 6, "col_id": "octane", "nombre": "Octane Booster Pro", "precio": "$2500", "img": "Octane.png", "detalle": """ MOTISI Octane Booster (modelo MZ323), un aditivo para combustible diseñado para mejorar el rendimiento del motor. Viene en una presentación de 400 ml y se promociona para su uso en motores de gasolina. 
Características y beneficios del producto
Según la publicidad y descripciones comerciales, este producto ofrece los siguientes beneficios:
Aumento de octanaje: Incrementa la potencia y maximiza el rendimiento del motor.
Aceleración mejorada: Optimiza la respuesta del acelerador, especialmente en rangos de carga baja y media.
Prevención de cascabeleo: Ayuda a prevenir detonaciones prematuras que pueden dañar el motor.
Limpieza del sistema: Contribuye a la limpieza de los inyectores y del sistema de combustible. 

"""}
]

@app.route('/')
def index():
    return render_template('index.html', colecciones=colecciones)

@app.route('/coleccion/<id_col>')
def ver_coleccion(id_col):
    col = next((c for c in colecciones if c['id'] == id_col), None)
    if not col: abort(404)
    items = [p for p in productos if p['col_id'] == id_col]
    return render_template('coleccion.html', coleccion=col, items=items)

@app.route('/producto/<int:id_prod>')
def detalle(id_prod):
    prod = next((p for p in productos if p['id'] == id_prod), None)
    if not prod: abort(404)
    return render_template('producto.html', p=prod)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
