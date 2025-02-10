FROM python:3.9

WORKDIR /app

# Copiar el archivo de dependencias y actualizar pip
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .
ENV PYTHONPATH=/app
CMD ["python", "app/main.py"]
