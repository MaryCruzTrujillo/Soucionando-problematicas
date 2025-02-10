from flask import Blueprint, jsonify
from app.services.data_analysis import DataAnalysisService

data_bp = Blueprint("data_analysis", __name__)
service = DataAnalysisService()

@data_bp.route("/clasificacion-ventas", methods=["GET"])
def clasificacion_ventas():
    return jsonify(service.classify_sales())

@data_bp.route("/desviacion-estandar", methods=["GET"])
def desviacion_estandar():
    return jsonify(service.calculate_standard_deviation())

@data_bp.route("/reporte", methods=["GET"])
def generar_reporte():
    return jsonify(service.generate_reports())

@data_bp.route("/graficos", methods=["GET"])
def generar_graficos():
    return service.generate_graphs()
