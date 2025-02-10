# 📦 API de Productos e Inventario

## 📖 Descripción
Esta API en Flask permite gestionar productos e inventarios, incluyendo operaciones CRUD y generación de gráficos de ventas. Se conecta a una base de datos PostgreSQL y cuenta con análisis de datos.

---

## 🚀 Instalación y Ejecución

### 🔹 Requisitos Previos
- Python 3.9+
- PostgreSQL
- Docker y Docker Compose (opcional, si se ejecuta con contenedores)

### 🏗️ Instalación Manual (Sin Docker)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crear un entorno virtual y activarlo:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   Crear un archivo `.env` y definir:
   ```env
   DATABASE_URL=postgresql://usuario:password@localhost:5432/tu_base_de_datos
   ```

5. Ejecutar la aplicación:
   ```bash
   flask run
   ```

---

### 🐳 Ejecución con Docker

1. Construir y levantar los contenedores:
   ```bash
   docker-compose up --build
   ```

2. La API estará disponible en:
   ```
   http://localhost:5000
   ```

3. Para detener los contenedores:
   ```bash
   docker-compose down
   ```

---

## 📌 Endpoints

### 📦 Productos
- **Obtener productos:** `GET /productos`
- **Crear producto:** `POST /productos`
- **Actualizar producto:** `PUT /productos/{id}`
- **Eliminar producto:** `DELETE /productos/{id}`
- **Generar gráfico de ventas:** `GET /productos/grafico`

### 📦 Inventario
- **Obtener inventario:** `GET /inventarios`
- **Obtener inventario de un producto:** `GET /inventario/{product_id}`
- **Actualizar stock de inventario:** `PUT /inventario/{product_id}`
- **Verificar reabastecimiento:** `GET /inventario/reabastecimiento/{product_id}`

### 📊 Análisis de Datos
- **Clasificación de ventas:** `GET /clasificacion-ventas`
- **Desviación estándar:** `GET /desviacion-estandar`
- **Generar reportes:** `GET /reporte`
- **Generar gráficos:** `GET /graficos`

---

## 🛠️ Tecnologías Utilizadas
- Python + Flask
- PostgreSQL
- SQLAlchemy
- Matplotlib
- Docker