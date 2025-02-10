import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from flask import send_file
from app.repositories.product_repository import ProductRepository

class DataAnalysisService:
    def __init__(self):
        self.repository = ProductRepository()

    def classify_sales(self):
        productos = self.repository.get_all()
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

    def calculate_standard_deviation(self):
        productos = self.repository.get_all()
        ventas = [p.ventas for p in productos]
        return {"desviacion_estandar": np.std(ventas)}

    def generate_reports(self):
        productos = self.repository.get_all()
        data = [{"nombre": p.nombre, "ventas": p.ventas, "inventario": p.inventario.stock_actual if p.inventario else 0} for p in productos]
        df = pd.DataFrame(data)

        report = {
            "media_ventas": df["ventas"].mean(),
            "mediana_ventas": df["ventas"].median(),
            "desviacion_estandar_ventas": df["ventas"].std(),
            "ventas_totales": df["ventas"].sum(),
            "productos_mas_vendidos": df.sort_values("ventas", ascending=False).head(3).to_dict(orient="records"),
        }
        return report

    def generate_graphs(self):
        productos = self.repository.get_all()
        data = [{"nombre": p.nombre, "ventas": p.ventas, "inventario": p.inventario.stock_actual if p.inventario else 0} for p in productos]
        df = pd.DataFrame(data)

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
        axes[1, 1].set_xticklabels(df["nombre"], rotation=45)

        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        return send_file(img, mimetype="image/png")
