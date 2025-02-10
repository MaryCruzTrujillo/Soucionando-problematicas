import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from flask import send_file, jsonify
from app.repositories.product_repository import ProductRepository

class DataAnalysisService:
    def __init__(self):
        self.repository = ProductRepository()

    def classify_sales(self):
        try:
            productos = self.repository.get_all()
            if not productos:
                return {"message": "No hay datos disponibles"}

            data = [{"nombre": p.nombre, "ventas": p.ventas} for p in productos]
            df = pd.DataFrame(data)

            def clasificar_ventas(ventas):
                if ventas > 1000:
                    return "Altas"
                elif 500 <= ventas <= 1000:
                    return "Medias"
                else:
                    return "Bajas"

            df["Clasificación"] = df["ventas"].apply(clasificar_ventas)
            return df.to_dict(orient="records")
        except Exception as e:
            return {"error": f"Error al clasificar ventas: {str(e)}"}

    def calculate_standard_deviation(self):
        try:
            productos = self.repository.get_all()
            if not productos:
                return {"message": "No hay datos disponibles"}

            ventas = [p.ventas for p in productos]
            return {"desviacion_estandar": float(np.std(ventas))}  # Asegurando serialización JSON
        except Exception as e:
            return {"error": f"Error al calcular la desviación estándar: {str(e)}"}

    def generate_reports(self):
        try:
            productos = self.repository.get_all()
            if not productos:
                return {"message": "No hay datos disponibles"}

            data = [
                {
                    "nombre": p.nombre,
                    "ventas": p.ventas,
                    "inventario": p.inventario.stock_actual if hasattr(p, 'inventario') and p.inventario else 0
                }
                for p in productos
            ]
            df = pd.DataFrame(data)

            if df.empty:
                return {"message": "No hay datos suficientes para generar un reporte"}

            report = {
                "media_ventas": float(df["ventas"].mean()),
                "mediana_ventas": float(df["ventas"].median()),
                "desviacion_estandar_ventas": float(df["ventas"].std()),
                "ventas_totales": int(df["ventas"].sum()),
                "productos_mas_vendidos": df.sort_values("ventas", ascending=False).head(3).to_dict(orient="records"),
            }
            return report
        except Exception as e:
            return {"error": f"Error al generar el reporte: {str(e)}"}

    def generate_graphs(self):
        try:
            productos = self.repository.get_all()
            if not productos:
                return jsonify({"message": "No hay datos disponibles"})

            data = [
                {
                    "nombre": p.nombre,
                    "ventas": p.ventas,
                    "inventario": p.inventario.stock_actual if p.inventario else 0
                }
                for p in productos
            ]
            df = pd.DataFrame(data)

            if df.empty:
                return jsonify({"message": "No hay datos suficientes para generar gráficos"})

            fig, axes = plt.subplots(2, 2, figsize=(12, 10))

            # Histograma de ventas
            sns.histplot(df["ventas"], bins=10, kde=True, ax=axes[0, 0])
            axes[0, 0].set_title("Distribución de Ventas")

            # Boxplot de ventas
            sns.boxplot(x=df["ventas"], ax=axes[0, 1])
            axes[0, 1].set_title("Boxplot de Ventas")

            # Gráfico de dispersión de inventario vs ventas
            sns.scatterplot(x=df["ventas"], y=df["inventario"], ax=axes[1, 0])
            axes[1, 0].set_title("Relación entre Ventas e Inventario")

            # Gráfico de barras de ventas por producto
            sns.barplot(x=df["nombre"], y=df["ventas"], ax=axes[1, 1])
            axes[1, 1].set_title("Ventas por Producto")
            axes[1, 1].set_xticklabels(df["nombre"], rotation=45, ha="right")

            plt.tight_layout()
            img = io.BytesIO()
            plt.savefig(img, format="png")
            img.seek(0)
            return send_file(img, mimetype="image/png")

        except Exception as e:
            return jsonify({"error": f"Error al generar gráficos: {str(e)}"})
