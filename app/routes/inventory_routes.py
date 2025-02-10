from flask import Blueprint, jsonify, request
from app.services.inventory_service import InventoryService

inventory_bp = Blueprint("inventory", __name__)
service = InventoryService()

@inventory_bp.route("/inventarios", methods=["GET"])
def get_inventory():
    inventory = service.get_all_inventory()
    return jsonify([{"id": i.id, "producto_id": i.producto_id, "stock_actual": i.stock_actual, "demanda_proyectada": i.demanda_proyectada, "nivel_reabastecimiento": i.nivel_reabastecimiento} for i in inventory])

# Crear un nuevo inventario
@inventory_bp.route("/inventarios", methods=["POST"])
def add_inventory():
    data = request.get_json()

    # Validación de campos obligatorios
    required_fields = ["producto_id", "stock_actual", "demanda_proyectada", "costo_mantenimiento"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({
            "message": f"Datos inválidos. Faltan los siguientes campos: {', '.join(missing_fields)}"
        }), 400

    # Creación del inventario
    new_inventory = service.create_inventory(data)
    if not new_inventory:
        return jsonify({"message": "No se pudo agregar el inventario"}), 500

    return jsonify({
        "message": "Inventario agregado",
        "id": new_inventory.id,
        "producto_id": new_inventory.producto_id,
        "stock_actual": new_inventory.stock_actual,
        "demanda_proyectada": new_inventory.demanda_proyectada,
        "nivel_reabastecimiento": new_inventory.nivel_reabastecimiento,
        "costo_mantenimiento": new_inventory.costo_mantenimiento
    }), 201

@inventory_bp.route("/inventario/<int:product_id>", methods=["GET"])
def get_inventory_by_product(product_id):
    inventory = service.get_inventory_by_product(product_id)
    if not inventory:
        return jsonify({"message": "Inventario no encontrado"}), 404
    return jsonify({"id": inventory.id, "producto_id": inventory.producto_id, "stock_actual": inventory.stock_actual, "demanda_proyectada": inventory.demanda_proyectada, "nivel_reabastecimiento": inventory.nivel_reabastecimiento})

@inventory_bp.route("/inventario/<int:product_id>", methods=["PUT"])
def update_inventory(product_id):
    data = request.json
    updated_inventory = service.update_inventory_stock(product_id, data["stock_actual"])
    if not updated_inventory:
        return jsonify({"message": "Inventario no encontrado"}), 404
    return jsonify({"message": "Inventario actualizado"})

@inventory_bp.route("/inventario/reabastecimiento/<int:product_id>", methods=["GET"])
def check_restock(product_id):
    needs_restock = service.check_inventory_restock(product_id)
    return jsonify({"producto_id": product_id, "necesita_reabastecimiento": needs_restock})
