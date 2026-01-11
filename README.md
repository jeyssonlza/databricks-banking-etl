# 🏦 ETL Pipeline - Transacciones Bancarias con Databricks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Databricks](https://img.shields.io/badge/Databricks-Latest-brightgreen)](https://databricks.com/)

## 📖 Descripción

Pipeline de ETL (Extract, Transform, Load) profesional para procesar transacciones bancarias multimoneda utilizando **Apache Spark**, **Databricks**, y **Delta Lake**. El proyecto automatiza la ingestión, transformación y análisis de datos financieros, generando una tabla de hechos optimizada para business intelligence.

### Características Principales
✅ Procesamiento de transacciones multimoneda (USD, Bolívares)  
✅ Conversión automática de monedas  
✅ Normalización de datos de clientes  
✅ Tabla Delta optimizada para análisis  
✅ Escalable a millones de registros  
✅ Documentación completa y código modular  

---

## 🏗️ Arquitectura del Proyecto

```
┌─────────────────────┐
│  Transacciones CSV  │
│  (Clientes JSON)    │
└──────────┬──────────┘
           │
           ▼
┌──────────────────────┐
│   Spark ETL Layer    │
│  ├─ Read CSV/JSON    │
│  ├─ Data Cleaning    │
│  └─ Normalization    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Transformations     │
│  ├─ Currency Conv.   │
│  ├─ Aggregations     │
│  └─ Date Processing  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Delta Lake         │
│ FactTransacciones    │
│  (Optimized Table)   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  BI & Analytics      │
│  SQL Queries         │
│  Dashboards          │
└──────────────────────┘
```

---

## 🛠️ Stack Tecnológico

| Componente | Versión | Propósito |
|---|---|---|
| **Databricks** | Latest | Plataforma cloud de datos |
| **Apache Spark** | 3.x | Motor de procesamiento |
| **Delta Lake** | Latest | Storage optimizado |
| **Python** | 3.11+ | Lenguaje de scripting |
| **SQL** | ANSI | Transformaciones avanzadas |

---

## 📁 Estructura del Repositorio

```
databricks-banking-etl/
├── README.md                          # Este archivo
├── LICENSE                            # Licencia MIT
├── .gitignore                         # Excepciones de Git
├── notebooks/                         # Notebooks de Databricks
│   ├── 01_load_transactions.py       # Carga de transacciones
│   ├── 02_load_customers.py          # Carga de clientes
│   ├── 03_transformations.py         # Transformaciones
│   └── 04_fact_table.py              # Generación de tabla de hechos
├── sql/                               # Scripts SQL
│   ├── create_schema.sql             # Creación de esquema
│   ├── queries_analysis.sql          # Queries de análisis
│   └── views.sql                     # Vistas útiles
├── data/                              # Datos de ejemplo
│   ├── sample_transactions.csv       # Datos de prueba
│   ├── sample_customers.json         # Clientes de prueba
│   └── README_DATA.md                # Documentación de datos
├── docs/                              # Documentación técnica
│   ├── ARCHITECTURE.md               # Diseño de arquitectura
│   ├── ETL_FLOW.md                   # Flujo ETL detallado
│   └── TROUBLESHOOTING.md            # Guía de solución de problemas
└── config/                            # Configuraciones
    ├── settings.py                   # Variables globales
    └── connections.py                # Conexiones a BD
```

---

## 🚀 Quick Start

### Requisitos Previos
- Cuenta activa en Databricks
- Cluster Databricks con Runtime 13.x+
- Datos en formato CSV y JSON

### 1. Clonar el Repositorio
```bash
git clone https://github.com/jeyssonlza/databricks-banking-etl.git
cd databricks-banking-etl
```

### 2. Configurar Notebook en Databricks
```python
# 1. Importar los notebooks desde GitHub
# 2. Actualizar rutas de datos según tu ambiente
# 3. Ejecutar secuencialmente: 01 → 02 → 03 → 04
```

### 3. Validar Resultados
```sql
SELECT COUNT(*) as total_transacciones FROM proyecto_bancario.FactTransacciones;
SELECT * FROM proyecto_bancario.FactTransacciones LIMIT 10;
```

---

## 📊 Flujo de Datos

### Etapa 1: Extracción (Extract)
- **CSV de Transacciones**: Lectura con delimitador `|`
- **JSON de Clientes**: Lectura con modo multiline
- Validaciones de integridad

### Etapa 2: Transformación (Transform)
```python
# Conversión de monedas
monto_BOLIVARES = WHEN moneda="USD" THEN monto * 4.5 ELSE monto

# Normalización de documentos
documento = LPAD(documento, 8, '0')

# Agregaciones por usuario/día
DEPOSITO = SUM(WHEN tipo_transaccion='DEPOSITO')
RETIRO = SUM(WHEN tipo_transaccion='RETIRO')
```

### Etapa 3: Carga (Load)
- Almacenamiento en Delta Lake
- Particionamiento por fecha
- Índices y optimizaciones

---

## 💾 Esquema de Datos

### Tabla: `FactTransacciones`
| Columna | Tipo | Descripción |
|---------|------|-------------|
| ClienteID | INT | Identificador único del cliente |
| Documento | STRING | Documento normalizado (8 dígitos) |
| NombreCompleto | STRING | Nombre del cliente |
| Fecha | DATE | Fecha de la transacción |
| Deposito | DECIMAL(18,2) | Monto total depositado en Bolívares |
| Retiro | DECIMAL(18,2) | Monto total retirado en Bolívares |

---

## 📈 Análisis Disponible

### Queries Ejemplo
```sql
-- Clientes más activos
SELECT NombreCompleto, COUNT(*) as transacciones
FROM FactTransacciones
GROUP BY NombreCompleto
ORDER BY transacciones DESC;

-- Volumen por día
SELECT Fecha, SUM(Deposito) as total_depositos, SUM(Retiro) as total_retiros
FROM FactTransacciones
GROUP BY Fecha
ORDER BY Fecha;

-- Balance por cliente
SELECT NombreCompleto, 
       SUM(Deposito) - SUM(Retiro) as balance
FROM FactTransacciones
GROUP BY NombreCompleto;
```

---

## 🔧 Configuración Avanzada

### Variables Personalizables
```python
# Rutas de datos
FILE_PATH_TRANSACCIONES = "/Volumes/workspace/proyecto_bancario/datasets/Transacciones.csv"
FILE_PATH_CLIENTES = "/Volumes/workspace/proyecto_bancario/datasets/Clientes.json"

# Esquema destino
TARGET_SCHEMA = "proyecto_bancario"
FACT_TABLE = "FactTransacciones"

# Parámetros de conversión
USD_TO_BOLIVARES = 4.5
```

### Optimizaciones Delta Lake
```python
# Vacío de datos no utilizados
VACUUM proyecto_bancario.FactTransacciones RETAIN 7 DAYS;

# Optimización de archivos
OPTIMIZE proyecto_bancario.FactTransacciones;
```

---

## 🧪 Testing & Validación

### Validaciones Implementadas
✅ Integridad referencial (cliente existe)  
✅ Tipos de dato correctos  
✅ Conversión de monedas verificada  
✅ Sin valores nulos en campos clave  
✅ Fechas dentro de rango válido  

```python
# Validar conteo de registros
assert df_transacciones.count() > 0, "No hay transacciones"
assert df_clientes.count() > 0, "No hay clientes"
assert df.count() == df_transacciones.count(), "Pérdida de datos en JOIN"
```

---

## 📚 Documentación Adicional

- [Arquitectura Detallada](./docs/ARCHITECTURE.md)
- [Flujo ETL Paso a Paso](./docs/ETL_FLOW.md)
- [Solución de Problemas](./docs/TROUBLESHOOTING.md)
- [Documentación de Datos](./data/README_DATA.md)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 Autor

**Jeysson Leoncio Z.**
Data Engineer | AI Automation Specialist

[LinkedIn](https://www.linkedin.com/in/jeysson-leoncio-z-712661249/) | [GitHub](https://github.com/jeyssonlza)283

---

## 📞 Soporte

Para preguntas o reportar bugs:
- Abre un Issue en GitHub
- Contacta en: [jeyssonzerpa@gmail.com]

---

## 🎯 Roadmap Futuro

- [ ] Integración con Power BI
- [ ] Alertas automáticas de fraude
- [ ] Machine Learning para predicciones
- [ ] API REST para consultas
- [ ] Dashboard interactivo en Databricks SQL
- [ ] Automatización con Databricks Jobs

---

**Actualizado**: Enero 2025
