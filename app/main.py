from flask import Flask
from app.database import init_db
from app.routes.product_routes import product_bp
from app.routes.inventory_routes import inventory_bp
from app.routes.data_analysis_routes import data_bp

app = Flask(__name__)

# Inicializar la base de datos
init_db()

# Registrar las rutas
app.register_blueprint(product_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(data_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
