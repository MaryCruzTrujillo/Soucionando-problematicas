from flask import Blueprint, jsonify, request, send_file
from app.services.product_service import ProductService
import matplotlib.pyplot as plt
import io

# Crear el Blueprint
product_bp = Blueprint("products", __name__)
service = ProductService()

# Obtener todos los productos
@product_bp.route("/productos", methods=["GET"])
def get_products():
    products = service.get_all_products()
    return jsonify([
        {"id": p.id, "nombre": p.nombre, "ventas": p.ventas, "inventario": p.inventario}
        for p in products
    ]), 200

# Crear un nuevo producto
@product_bp.route("/productos", methods=["POST"])
def create_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos inválidos o JSON vacío"}), 400

    # Verifica si data es una lista y toma el primer elemento si es necesario
    if isinstance(data, list):
        data = data[0]

    if not isinstance(data, dict):
        return jsonify({"error": "El formato del JSON debe ser un objeto, no una lista"}), 400

    product = service.create_product(data)

    if not product:
        return jsonify({"error": "No se pudo crear el producto"}), 500
    
    return jsonify({"message": "Producto agregado", "id": product.id}), 201


# Actualizar un producto existente
@product_bp.route("/productos/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos o JSON vacío"}), 400

    updated_product = service.update_product(id, data)
    if not updated_product:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    return jsonify({"message": "Producto actualizado"}), 200

# Eliminar un producto
@product_bp.route("/productos/<int:id>", methods=["DELETE"])
def delete_product(id):
    if service.delete_product(id):
        return jsonify({"message": "Producto eliminado"}), 200
    
    return jsonify({"error": "Producto no encontrado"}), 404

# Generar gráfico de ventas por producto
@product_bp.route("/productos/grafico", methods=["GET"])
def generar_grafico():
    products = service.get_all_products()

    if not products:
        return jsonify({"error": "No hay productos disponibles"}), 404

    nombres = [p.nombre for p in products]
    ventas = [p.ventas for p in products]

    plt.figure(figsize=(8,5))
    plt.bar(nombres, ventas, color='blue')
    plt.xlabel('Productos')
    plt.ylabel('Ventas')
    plt.title('Ventas por Producto')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()  # Evita saturación de memoria por múltiples gráficos

    return send_file(img, mimetype='image/png')
