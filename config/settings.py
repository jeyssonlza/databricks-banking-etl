"""
Configuraciones generales del proyecto ETL Bancario
"""

# ==================== RUTAS DE DATOS ====================
VOLUME_PATH = "/Volumes/workspace/proyecto_bancario"
DATASETS_PATH = f"{VOLUME_PATH}/datasets"

# Archivos de entrada
FILE_PATH_TRANSACCIONES = f"{DATASETS_PATH}/Transacciones.csv"
FILE_PATH_CLIENTES = f"{DATASETS_PATH}/Clientes.json"

# ==================== ESQUEMAS Y TABLAS ====================
TARGET_SCHEMA = "proyecto_bancario"
FACT_TABLE = "FactTransacciones"
DIM_CLIENTES = "DimClientes"

# ==================== PARAMETROS DE PROCESAMIENTO ====================
# Delimitador del CSV
CSV_DELIMITER = "|"

# Encoding
FILE_ENCODING = "utf-8"

# Modo de guardar
SAVE_MODE = "overwrite"  # overwrite, append, ignore, error
FORMAT = "delta"

# ==================== CONVERSION DE MONEDAS ====================
USD_TO_BOLIVARES = 4.5
BANK_CURRENCY = "VES"  # Venezuelan Bolívares

# ==================== VALIDACIONES ====================
# Campos requeridos
REQUIRED_TRANSACTION_FIELDS = [
    "id_usuario",
    "tipo_transaccion",
    "moneda",
    "monto",
    "fecha_transaccion"
]

REQUIRED_CLIENT_FIELDS = [
    "id_usuario",
    "documento",
    "nombre"
]

# Tipos de transaccion validos
VALID_TRANSACTION_TYPES = ["DEPOSITO", "RETIRO"]
VALID_CURRENCIES = ["USD", "VES"]

# ==================== FORMATO DE DOCUMENTOS ====================
DOCUMENT_LENGTH = 8  # Longitud estandar de documento

# ==================== LOGGING ====================
LOG_LEVEL = "INFO"
LOG_PATH = f"{VOLUME_PATH}/logs"

# ==================== OPTIMIZACIONES ====================
# Particionar por:
PARTITION_BY = "fecha"  # Particionar tabla de hechos por fecha

# Número de particiones para shuffle
NUM_SHUFFLES = 200

# ==================== CACHE ====================
ENABLE_CACHE = True
