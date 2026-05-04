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
    {"id": 1, "col_id": "aceites", "nombre": "Aceite SAE 10W-40", "precio": "$8500", "img": "Aceite SAE 10W-40.png", "detalle": """aceite sintético multiuso Motisi SAE 10W-40, un lubricante diseñado para motores de gasolina y diésel. Se comercializa principalmente en Cuba (específicamente en regiones como La Habana y Marianao) en un formato de 5 litros. [1, 2, 3, 4]

Detalles del producto

Viscosidad: SAE 10W-40, lo que indica un buen desempeño tanto en arranques en frío como en temperaturas de operación calientes.

Compatibilidad: Apto para motores de gasolina y diésel. Algunas especificaciones encontradas en productos similares de la marca mencionan clasificaciones API SL/CF o CI-4/SL.

Beneficios promocionados: La publicidad resalta una protección total, mayor eficiencia y un arranque en frío óptimo.

"""},
    {"id": 2, "col_id": "aceites", "nombre": "Aceite SAE 15W-40", "precio": "$8500", "img": "Aceite SAE 15W-40.png", "detalle": "Rendimiento superior en carretera. Mantiene el motor limpio."},
    {"id": 3, "col_id": "aceites", "nombre": "Aceite SAE 20W-50", "precio": "$8500", "img": "Aceite SAE 20W-40.png", "detalle": "Para motores de alta exigencia que buscan sellado y potencia."},
    {"id": 4, "col_id": "grasas", "nombre": "Super Grease MP-3 (Verde)", "precio": "$1800", "img": "Grasa de Litio.png", "detalle": "Base de Litio. Perfecta para rodamientos de alta velocidad."},
    {"id": 5, "col_id": "grasas", "nombre": "Multi-Purpose AP-2 (Roja)", "precio": "$1600", "img": "Grasa Azul Multiuso.png", "detalle": "Grasa multiuso reforzada. Resistente al agua y fricción."},
    {"id": 6, "col_id": "octane", "nombre": "Octane Booster Pro", "precio": "$2500", "img": "Octane.png", "detalle": "Sube el octanaje y elimina el cascabeleo. Más fuerza al acelerar."}
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
