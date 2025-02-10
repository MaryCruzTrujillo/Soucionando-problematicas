# 📦 API de Gestión de Inventarios y Productos

## 🛠️ Descripción
Esta API permite gestionar productos e inventarios, proporcionando funciones para agregar, actualizar, eliminar y consultar información sobre productos y su inventario. También incluye endpoints para análisis de datos y generación de gráficos.

---

## 🚀 Instalación y Ejecución con Docker

### 1️⃣ **Clonar el repositorio**
```sh
 git clone https://github.com/tu-repositorio.git
 cd tu-repositorio
```

### 2️⃣ **Ejecutar con Docker**
```sh
docker-compose up --build
```
Esto iniciará la aplicación Flask junto con PostgreSQL.

---

## 🛠️ **Rutas Disponibles**

### 🛒 **Productos**

📌 **Obtener todos los productos**
```sh
curl -X GET http://localhost:5000/productos
```

📌 **Agregar un nuevo producto**
```sh
curl -X POST http://localhost:5000/productos \
     -H "Content-Type: application/json" \
     -d '{
        "nombre": "Laptop Gamer",
        "ventas": 50,
        "descripcion": "Intel i7, 16GB RAM, SSD 512GB"
        }
'
```

📌 **Actualizar un producto**
```sh
curl -X PUT http://localhost:5000/productos/1 \
     -H "Content-Type: application/json" \
     -d '{
           "nombre": "Laptop Pro",
           "ventas": 250,
           "inventario": 40
         }'
```

📌 **Eliminar un producto**
```sh
curl -X DELETE http://localhost:5000/productos/1
```

📌 **Generar gráfico de ventas por producto**
```sh
curl -X GET http://localhost:5000/productos/grafico
```

---

### 📦 **Inventarios**

📌 **Obtener todos los inventarios**
```sh
curl -X GET http://localhost:5000/inventarios
```

📌 **Agregar un inventario**
```sh
curl -X POST http://localhost:5000/inventarios \
     -H "Content-Type: application/json" \
     -d '{
           "producto_id": 1,
           "stock_actual": 100,
           "demanda_proyectada": 50,
           "costo_mantenimiento": 15.75
         }'
```

📌 **Obtener inventario de un producto**
```sh
curl -X GET http://localhost:5000/inventario/1
```

📌 **Actualizar stock de un inventario**
```sh
curl -X PUT http://localhost:5000/inventario/1 \
     -H "Content-Type: application/json" \
     -d '{
           "stock_actual": 120
         }'
```

📌 **Verificar si un producto necesita reabastecimiento**
```sh
curl -X GET http://localhost:5000/inventario/reabastecimiento/1
```

---

### 📊 **Análisis de Datos**

📌 **Clasificación de ventas**
```sh
curl -X GET http://localhost:5000/clasificacion-ventas
```

📌 **Calcular desviación estándar**
```sh
curl -X GET http://localhost:5000/desviacion-estandar
```

📌 **Generar reporte de datos**
```sh
curl -X GET http://localhost:5000/reporte
```

📌 **Generar gráficos de datos**
```sh
curl -X GET http://localhost:5000/graficos
```

---

## 🛠️ **Tecnologías Utilizadas**
- Python (Flask)
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- Matplotlib (para gráficos)

---

## 📌 **Notas Adicionales**
- Asegúrate de tener Docker y Docker Compose instalados.
- Si hay problemas de conexión con la base de datos, revisa el archivo `docker-compose.yml`.

🚀 ¡Ahora puedes gestionar productos e inventarios de manera eficiente con esta API! 🎉

