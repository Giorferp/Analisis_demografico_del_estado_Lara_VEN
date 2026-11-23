# Análisis Demográfico y Reconstrucción Cuantitativa Censal: Estado Lara, Venezuela

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-managed-6B5CE7)](https://docs.astral.sh/uv/)
[![SQLite](https://img.shields.io/badge/SQLite-60%20Tablas-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![XeLaTeX](https://img.shields.io/badge/XeLaTeX-APA%207-008080?logo=latex&logoColor=white)](https://www.tug.org/xetex/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Estudio demográfico integral y pipeline de ingeniería de datos aplicado al **Estado Lara (Venezuela)** sobre los microdatos y tabulados oficiales del **XIV Censo Nacional de Población y Vivienda 2011** (INE / REDATAM+SP), estadísticas vitales (MPPS) y series de la Encuesta de Hogares por Muestreo (EHM).

---

## 1. Entregables Principales para Presentación

| Entregable | Ruta | Descripción |
| :--- | :--- | :--- |
| **Informe Técnico Compilado (PDF)** | [`report/Análisis_Demográfico_del_Estado_Lara.pdf`](report/Análisis_Demográfico_del_Estado_Lara.pdf) | Memoria analítica de 23 páginas en formato APA 7 (XeLaTeX + Times New Roman), con 16 cuadros y 4 figuras vectoriales. |
| **Manuscrito Fuente (LaTeX)** | [`report/Análisis_Demográfico_del_Estado_Lara.tex`](report/Análisis_Demográfico_del_Estado_Lara.tex) | Fuente tipográfica reproducible del informe y sus 16 cuadros canónicos. |
| **Cuaderno Interactivo (Jupyter)** | [`notebooks/Análisis_Demográfico_del_Estado_Lara.ipynb`](notebooks/Análisis_Demográfico_del_Estado_Lara.ipynb) | Notebook ejecutado conectado a SQLite con consultas SQL, tablas formateadas y gráficos. |
| **Base Relacional Canónica** | [`data/processed/demografia_lara.db`](data/processed/demografia_lara.db) | Base SQLite auditada con 60 tablas (microdatos volcados, cruces IPF y tablas de vida). |
| **Figuras Vectoriales** | [`report/figures/`](report/figures/) | Cuatro gráficos vectoriales PDF nativos (`fig_lara_1.pdf` a `fig_lara_4.pdf`). |

---

## 2. Arquitectura del Proyecto

```text
.
├── README.md                                       # Documentación principal y guía de reproducibilidad
├── pyproject.toml                                  # Dependencias Python gestionadas con uv
├── .gitignore                                      # Exclusión de entornos, caches y auxiliares LaTeX
├── data/
│   ├── raw/                                        # 62 tabulados originales INE / REDATAM (.xls, .xlsx)
│   └── processed/
│       └── demografia_lara.db                      # Base SQLite canónica y auditada (60 tablas)
├── src/
│   ├── build_database.py                           # Parsers puros Python (SYLK/BIFF8/XLSX) + cruces ETL
│   ├── build_notebook.py                           # Generador programático del cuaderno Jupyter
│   ├── generate_figures.py                         # Generación de figuras vectoriales desde SQLite
│   └── build_report.py                             # Compilación reproducible a PDF vía XeLaTeX
├── notebooks/
│   └── Análisis_Demográfico_del_Estado_Lara.ipynb  # Cuaderno interactivo ejecutado (43 celdas)
├── report/
│   ├── Análisis_Demográfico_del_Estado_Lara.pdf    # Informe final compilado (23 páginas)
│   ├── Análisis_Demográfico_del_Estado_Lara.tex    # Código fuente LaTeX
│   └── figures/
│       ├── fig_lara_1.pdf                          # Pirámide quinquenal Lara vs. Venezuela
│       ├── fig_lara_2.pdf                          # Analfabetismo por cohortes y disparidad municipal
│       ├── fig_lara_3.pdf                          # Estructura conyugal y trayectoria etaria (≥ 15 años)
│       └── fig_lara_4.pdf                          # Fuerza de trabajo, formalidad y ramas de actividad
└── docs/
    ├── NOMENCLATURA_OFICIAL.md                     # Estándar terminológico, notación matemática y estilo
    └── audit/                                      # Dictámenes de auditoría numérica, tabular y estilo
        ├── AUDITORIA_TABLAS_LARA.md
        ├── AUDITORIA_NUMERICA_LARA.md
        ├── CERTIFICACION_FINAL_LARA.md
        └── DICTAMEN_AUDITORIA_CUANTITATIVA_FINAL_LARA.md
```

---

## 3. Síntesis Cuantitativa (Censo 2011 y Proyección 2016)

- **Volumen y Distribución Territorial:** $1.774.867$ habitantes ($883.775$ hombres; $891.092$ mujeres; $\text{IM} = 99{,}18$) sobre $19.800\text{ km}^2$ ($89{,}64\text{ hab./km}^2$). La conurbación Iribarren–Palavecino concentra el $65{,}94\%$ de la población en el $16{,}16\%$ del territorio.
- **Estructura Etaria y Bono Demográfico:** $26{,}94\%$ menores de 15 años ($478.217$), $66{,}90\%$ entre 15 y 64 años ($1.187.304$) y $6{,}16\%$ adultos mayores de 65 años y más ($109.346$); Edad Mediana $Me = 27{,}54$ años y Razón de Dependencia Total $\text{RDD} = 49{,}49$.
- **Capital Humano y Situación Conyugal:** Tasa de analfabetismo de $5{,}56\%$ en población $\ge 10$ años ($81.340$ de $1.463.542$ residentes). En población declarante $\ge 15$ años ($1.289.325$), el $50{,}53\%$ está casado o unido, $40{,}72\%$ soltero y $8{,}75\%$ disuelto (razón $1{,}13$ uniones consensuales por matrimonio civil).
- **Mercado Laboral ($\ge 15$ años):** En Censo 2011, $\text{PET} = 1.296.650$, $\text{PEA} = 794.846$ ($\text{TAE} = 61{,}30\%$), $\text{PO} = 731.258$ ($\text{TO} = 92{,}00\%$) y $\text{PD} = 63.588$ ($\text{TD} = 8{,}00\%$). La EHM calibra una ocupación de $701.209$ puestos ($58{,}00\%$ formal y $42{,}00\%$ informal; $66{,}00\%$ en el sector terciario).
- **Mortalidad y Proyección 2011–2016:** Tasa Bruta de Mortalidad observada de $5{,}14\text{‰}$ que desciende a $4{,}96\text{‰}$ al tipificar directamente contra Venezuela ($5{,}02\text{‰}$); esperanza de vida al nacer $e_0^0 = 74{,}42$ años ($77{,}56$ mujeres; $71{,}48$ hombres). La proyección por componentes sitúa la población en $1.874.973$ habitantes para 2016.

---

## 4. Flujo de Trabajo y Reproducibilidad

El proyecto utiliza **`uv`** para la gestión reproducible de dependencias Python y **XeLaTeX** para la compilación tipográfica del informe.

```bash
# 1. Regenerar las 4 figuras vectoriales (report/figures/fig_lara_1..4.pdf) desde SQLite
uv run python src/generate_figures.py

# 2. Compilar el informe final en PDF (report/Análisis_Demográfico_del_Estado_Lara.pdf)
uv run python src/build_report.py

# 3. Regenerar la estructura del cuaderno Jupyter (opcional)
uv run python src/build_notebook.py

# 4. Ejecutar el cuaderno interactivo desde la raíz o desde notebooks/
uv run --with jupyterlab jupyter lab notebooks/Análisis_Demográfico_del_Estado_Lara.ipynb
```

> **Nota sobre la base de datos (`data/processed/demografia_lara.db`):** La base SQLite incluida constituye el artefacto relacional auditado con 60 tablas (incluyendo las tablas base del Censo 2011, los cruces IPF, las tablas de vida Reed-Merrell y las conciliaciones descritas en `docs/audit/`). El script [`src/build_database.py`](src/build_database.py) implementa los parsers en librería estándar pura (`SYLK`, `BIFF8`, `XLSX`) y protege el archivo auditado exigiendo el argumento explícito `--rebuild` para evitar sobrescrituras accidentales.

---

## 5. Fuentes y Marco Legal

- **Fuentes Oficiales:** Instituto Nacional de Estadística (INE — XIV Censo Nacional de Población y Vivienda 2011, REDATAM+SP, Encuesta de Hogares por Muestreo) y Ministerio del Poder Popular para la Salud (MPPS — Anuario de Mortalidad 2011).
- **Naturaleza Académica:** Investigación desarrollada en la Cátedra de Demografía, Escuela de Estadística y Ciencias Actuariales (EECA), Facultad de Ciencias Económicas y Sociales (FACES), **Universidad Central de Venezuela (UCV)**.
- **Licencia y Reserva Estadística:** Todos los insumos corresponden a agregados macroestadísticos públicos y anónimos (Art. 22 de la Ley de la Función Pública de Estadística; Art. 44 de la Ley sobre el Derecho de Autor). Código bajo licencia **CC BY-NC-SA 4.0**.
