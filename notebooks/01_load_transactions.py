# Databricks notebook source
"""
Notebook 01: Load Banking Transactions

Este notebook carga transacciones bancarias desde un archivo CSV
y las prepara para procesamiento en el pipeline ETL.

Autor: Jeysson Laza
Fecha: Enero 2025
"""

# COMMAND ----------

# Configuracion inicial
from pyspark.sql.types import *
from pyspark.sql.functions import *
from datetime import datetime

print(f"Iniciando carga de transacciones - {datetime.now()}")

# COMMAND ----------

# Rutas de datos
FILE_PATH_TRANSACCIONES = "/Volumes/workspace/proyecto_bancario/datasets/Transacciones.csv"
SCHEMA_NAME = "proyecto_bancario"

print(f"Leyendo archivo: {FILE_PATH_TRANSACCIONES}")

# COMMAND ----------

# Definir esquema para el CSV
schema = StructType([
    StructField("id_usuario", IntegerType(), True),
    StructField("tipo_transaccion", StringType(), True),
    StructField("moneda", StringType(), True),
    StructField("monto", DoubleType(), True),
    StructField("fecha_transaccion", TimestampType(), True)
])

# COMMAND ----------

# Lectura del CSV
df_transacciones = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("sep", "|") \
    .schema(schema) \
    .load(FILE_PATH_TRANSACCIONES)

print(f"Total de transacciones cargadas: {df_transacciones.count()}")

# COMMAND ----------

# Mostrar primeros 10 registros
display(df_transacciones.limit(10))

# COMMAND ----------

# Validaciones basicas
print(f"Esquema del DataFrame:")
df_transacciones.printSchema()

print(f"\nEstadísticas de datos:")
df_transacciones.describe().show()

# COMMAND ----------

# Guardar en cache para reutilizacion
df_transacciones.cache()
print("DataFrame cacheado exitosamente")
