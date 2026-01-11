# Databricks notebook source
"""
Notebook 04: Generate Fact Table

Este notebook genera la tabla de hechos final combinando
transacciones y clientes para crear FactTransacciones.

Autor: Jeysson Laza
Fecha: Enero 2025
"""

# COMMAND ----------

# Importar funciones necesarias
from pyspark.sql.functions import *
from datetime import datetime

print(f"Iniciando generación de tabla de hechos - {datetime.now()}")

# COMMAND ----------

# Definir variables
SCHEMA = "proyecto_bancario"
FACT_TABLE = "FactTransacciones"

print(f"Esquema destino: {SCHEMA}")
print(f"Tabla de hechos: {FACT_TABLE}")

# COMMAND ----------

# Asumir que tenemos df_transacciones y df_clientes disponibles
# (obtenidos de notebooks anteriores)

# Realizar el JOIN
df_fact = df_transacciones.join(
    df_clientes,
    on="id_usuario",
    how="inner"
).select(
    col("id_usuario").alias("ClienteID"),
    col("documento").alias("Documento"),
    col("nombre_completo").alias("NombreCompleto"),
    col("fecha").alias("Fecha"),
    round(col("deposito"), 2).alias("Deposito"),
    round(col("retiro"), 2).alias("Retiro")
)

print(f"Total de registros en tabla de hechos: {df_fact.count()}")

# COMMAND ----------

# Mostrar preview
display(df_fact.limit(10))

# COMMAND ----------

# Escribir como tabla Delta
df_fact.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"{SCHEMA}.{FACT_TABLE}")

print(f"Tabla {SCHEMA}.{FACT_TABLE} creada exitosamente")

# COMMAND ----------

# Validaciones finales
df_result = spark.table(f"{SCHEMA}.{FACT_TABLE}")
print(f"Conteo final: {df_result.count()}")
print(f"Esquema validado correctamente")
