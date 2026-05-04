from flask import Flask, render_template, abort

app = Flask(__name__)

colecciones = [
    {"id": "aceites", "nombre": "Aceites Motor", "img": "Coleccion Aceite.png", "desc": "Máxima vida para tu motor con calidad Premium."},
    {"id": "grasas", "nombre": "Grasas Pro", "img": "Coleccion Grasa.png", "desc": "Lubricación extrema para rodamientos y piezas."},
    {"id": "octane", "nombre": "Aditivos", "img": "Octane.png", "desc": "Potencia extra y limpieza de inyectores."}
]

productos = [
    {"id": 1, "col_id": "aceites", "nombre": "Aceite SAE 10W-40", "precio": "$14000", "img": "Aceite SAE 10W-40.png", "detalle": "Aceite Sintético Multiuso Motisi SAE 10W-40. Formato de 5 litros. Protección total y arranque en frío óptimo."},
    {"id": 2, "col_id": "aceites", "nombre": "Aceite SAE 15W-40", "precio": "$14000", "img": "Aceite SAE 15W-40.png", "detalle": "Tecnología Japonesa API:CI-4/SL. Ideal para motores diésel de servicio pesado y gasolina."},
    {"id": 3, "col_id": "aceites", "nombre": "Aceite SAE 20W-50", "precio": "$14000", "img": "Aceite SAE 20W-40.png", "detalle": "Ideal para climas cálidos y motores de alto kilometraje. Certificación API CI-4/SL."},
    {"id": 4, "col_id": "grasas", "nombre": "Grasa de Litio", "precio": "$5000", "img": "Grasa de Litio.png", "detalle": "Alto rendimiento para maquinaria pesada. Resistente al agua y humedad."},
    {"id": 5, "col_id": "grasas", "nombre": "Grasa Azul Multiuso", "precio": "$5000", "img": "Grasa Azul Multiuso.png", "detalle": "Fórmula EP2 para altas temperaturas. Excelente adherencia en rodamientos."},
    {"id": 6, "col_id": "octane", "nombre": "Octane Booster Pro", "precio": "$3000", "img": "Octane.png", "detalle": "Aumenta el octanaje y optimiza la aceleración. Presentación de 400ml."}
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
    app.run() # Render configurará el puerto automáticamente
