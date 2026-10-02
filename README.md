# Análisis Demográfico y Reconstrucción Cuantitativa de Datos Censales: Estado Lara, Venezuela
## Demographic Analysis & Quantitative Census Data Reconstruction: Lara State, Venezuela

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Academic%20Research-success)](#marco-legal-y-descargo-de-responsabilidad)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

*Idiomas / Languages:* **[Español](#versión-en-español)** | **[English](#english-version)**

---

<a name="versión-en-español"></a>
# Versión en Español

## 1. Resumen Ejecutivo y Alcance del Proyecto
Este repositorio alberga una investigación cuantitativa y un pipeline de ingeniería de datos demográficos aplicado al **Estado Lara, Venezuela**. El objetivo central es modelar la dinámica demográfica, estructura etaria, condiciones educativas (alfabetismo y nivel de instrucción), patrones de nupcialidad/estado conyugal e indicadores macroeconómicos de la fuerza de trabajo.

El proyecto abarca desde la **ingeniería inversa y extracción automatizada de formatos legados (SYLK/REDATAM)** hasta la **reconciliación matemática de matrices multidimensionales (Ajuste Proporcional Iterativo / Algoritmo RAS)** y el modelado y procesamiento estructurado de tabulados con **Python (Pandas/NumPy)**.

---

## 2. Capacidades Técnicas y Aporte Cuantitativo (Highlights para Reclutadores)

* **Pipelines de Extracción y Parsing ETL para Formatos Propietarios (SYLK):**
  Desarrollo de parsers robustos desde cero en Python para procesar archivos de intercambio simbólico (`SYLK`) generados por el motor de microdatos *Redatam+SP* del INE/CEPAL, los cuales no son interpretables por librerías estándar como `openpyxl` o `xlrd`.
* **Reconstrucción Multidimensional mediante Máxima Entropía (IPF / Algoritmo RAS):**
  Ante la limitación del servidor censal que solo ofrecía tablas marginales bidimensionales ($2\text{D}$), se implementó el algoritmo de **Ajuste Proporcional Iterativo (Deming-Stephan)** para resolver el problema de optimización bajo información parcial:
  $$\min \sum_{i,j,k} N_{i,j,k} \ln\left(\frac{N_{i,j,k}}{N^0_{i,j,k}}\right)$$
  sujeto al cumplimiento simultáneo de las restricciones marginales oficiales por edad, sexo y condición educativa, garantizando exactitud matemática celda por celda sin alterar los agregados censales.
* **Armonización y Modelado de Datos Geoestadísticos (Pandas):**
  Construcción de estructuras matriciales e indexación jerárquica (`MultiIndex`) para articular datos a nivel de entidad federal, municipio y parroquia mediante identificadores geoestadísticos normados (`Código UBIGEO`), garantizando la integridad de agregaciones transversales entre censos, registros continuos y encuestas por muestreo.
* **Rigor Metodológico Demográfico:**
  Segmentación analítica estricta según los universos censales de las variables:
  * *Población general:* Cohortes quinquenales desde $0$ a $4$ hasta $95$ y más años.
  * *Alfabetismo y Nivel de Instrucción:* Población de $10$ años y más ($\ge 10$).
  * *Situación Conyugal:* Población de $12$ años y más ($\ge 12$).
  * *Fuerza de Trabajo:* Población en Edad de Trabajar según estándares internacionales OIT/INE ($\ge 15$ años).

---

## 3. Estructura del Repositorio

```text
├── Análisis_Demográfico_del_Estado_Lara.ipynb   # Notebook principal de análisis y tabulaciones
├── alfabetismo.xlsx                             # Dataset limpio de alfabetismo (Edad, Sexo y Cruce)
├── situacion_conyugal.xlsx                      # Dataset limpio de situación conyugal (Hombres, Mujeres, Total)
├── nivel_instruccion.xlsx                       # Dataset limpio de nivel educativo formal
├── TRABAJO.xlsx                                 # Series históricas oficiales de la EHM (1999-2025)
├── Lara.xls                                     # Microdatos censales de centros poblados e infraestructura
├── Poblacion-*.xlsx                             # Tabulados base de población por sexo, edad y origen
├── Servicios-Censo_2011.xlsx                    # Cobertura de servicios básicos por parroquia
├── VIVIENDAS-HOGARES-Y-PERSONAS-CENSO-2011.xlsx # Agregados de vivienda, hogar y personas por UBIGEO
└── README.md                                    # Documentación técnica, metodológica y legal
```

---

## 4. Fuentes de Datos y Procedencia
Todos los datos utilizados en esta investigación provienen de fuentes oficiales del Estado venezolano y organismos internacionales de estadística:

1. **Instituto Nacional de Estadística (INE), República Bolivariana de Venezuela:**
   * **XIV Censo Nacional de Población y Vivienda (2011):** Microdatos agregados procesados a través del servidor en línea *Redatam+SP* (CEPAL/CELADE) y publicaciones oficiales del empadronamiento de viviendas, hogares y personas.
   * **Encuesta de Hogares por Muestreo (EHM):** Indicadores Globales de la Fuerza de Trabajo, 1eros Semestres 1999–2025 (Cuadros de ocupación, sector formal/informal, ramas CIIU y nivel educativo).
   * **Estadísticas Vitales y Demográficas:** Registros continuos de nacimientos y matrimonios por entidad y municipio.
2. **CELADE - División de Población de la CEPAL (Comisión Económica para América Latina y el Caribe):**
   * Metodologías y estándares del software *Redatam+SP* (*Retrieval of Data for Small Areas by Microcomputer*).

---

## 5. Marco Legal, Naturaleza Académica y Exención de Responsabilidad

> [!IMPORTANT]
> ### Declaración de Naturaleza Estrictamente Académica
> El presente proyecto constituye un trabajo de investigación científica, cuantitativa y pedagógica desarrollado en el marco de estudios demográficos de pregrado en la **Universidad Central de Venezuela (UCV)**. Su único propósito es la formación profesional, el modelado estadístico y la divulgación de habilidades analíticas en ciencia de datos.

### Cumplimiento de la Legislación Venezolana e Internacional

1. **Principio de Secreto y Reserva Estadística:**
   En estricto cumplimiento del **Artículo 22 y concordantes de la Ley de la Función Pública de Estadística** de la República Bolivariana de Venezuela, este repositorio **NO contiene, manipula ni expone datos nominativos individuales, privados ni confidenciales**. Toda la información procesada corresponde a agregados macroestadísticos y tabulados censales de dominio público anonimizados por el INE.
2. **Uso Legítimo con Fines Académicos y de Investigación (Fair Use):**
   De conformidad con el **Artículo 44 (numerales 1 y 2) de la Ley sobre el Derecho de Autor de Venezuela** y los tratados internacionales de propiedad intelectual (Convenio de Berna), es lícita la utilización, reproducción y análisis de datos e informes oficiales de acceso público con fines estrictamente didácticos, de investigación científica y sin fines de lucro comercial.
3. **Exención de Responsabilidad Oficial (Disclaimer):**
   Este proyecto es un análisis independiente realizado por estudiantes/investigadores y **no representa una posición oficial, dictamen institucional o certificación legal** del Instituto Nacional de Estadística (INE), del Gobierno de Venezuela, ni de la CEPAL. Ni el autor ni las instituciones académicas vinculadas asumen responsabilidad por el uso o interpretación secundaria que terceros hagan de estos modelos.
4. **Licenciamiento de Código:**
   El código fuente de extracción, pipelines ETL y modelado cuantitativo está disponible bajo los términos de la licencia **Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)**.

---

<a name="english-version"></a>
# English Version

## 1. Executive Summary & Project Scope
This repository houses an advanced quantitative study and demographic data engineering pipeline focused on **Lara State, Venezuela**. The primary objective is to analyze and model population dynamics, age-sex structures, educational metrics (literacy and formal schooling), nuptiality/marital patterns, and macroeconomic labor force indicators.

The technical workflow spans **reverse-engineering and parsing legacy data formats (SYLK/REDATAM)**, **multidimensional matrix reconciliation via Iterative Proportional Fitting (IPF / RAS algorithm)**, and structured multidimensional data processing and modeling using **Python (Pandas/NumPy)**.

---

## 2. Technical Capabilities & Quantitative Highlights (For Recruiters)

* **Legacy Data Parsing & Custom ETL Pipelines (SYLK):**
  Engineered custom text-stream parsers in pure Python to process symbolic link (`SYLK`) spreadsheets generated by the UN-ECLAC/INE *Redatam+SP* census engine, bypassing failures in standard libraries (`openpyxl`, `xlrd`).
* **Multidimensional Contingency Table Reconciliation (IPF / RAS Algorithm):**
  Overcame public census platform limitations (which only provided disjoint 2D marginal distributions) by implementing an **Iterative Proportional Fitting (Deming-Stephan algorithm)** pipeline under maximum entropy constraints:
  $$\min \sum_{i,j,k} N_{i,j,k} \ln\left(\frac{N_{i,j,k}}{N^0_{i,j,k}}\right)$$
  subject to exact preservation of known age, sex, and educational category marginals, ensuring cell-by-cell mathematical consistency without altering census totals.
* **Geostatistical Data Harmonization & Tabular Modeling (Pandas):**
  Engineered multi-level hierarchical indexing (`MultiIndex`) and standardized tabular structures across federal, municipal, and parish tiers using official geo-statistical codes (`UBIGEO`), ensuring seamless cross-sectional aggregations and mathematical consistency across censuses, civil registries, and household surveys.
* **Demographic Methodological Rigor:**
  Enforced precise census universe boundaries:
  * *Total Population:* Standard 5-year cohorts from $0\text{--}4$ to $95+$.
  * *Literacy & Formal Education:* Population aged 10 and older ($\ge 10$).
  * *Marital Status:* Population aged 12 and older ($\ge 12$), reflecting legal/census eligibility.
  * *Labor Force & Economic Activity:* Working Age Population ($\ge 15$), strictly adhering to ILO/INE standards.

---

## 3. Repository Architecture

```text
├── Análisis_Demográfico_del_Estado_Lara.ipynb   # Main Jupyter notebook with analytical pipelines
├── alfabetismo.xlsx                             # Reconciled literacy dataset (Age, Sex, Joint)
├── situacion_conyugal.xlsx                      # Standardized marital status dataset (Men, Women, Total)
├── nivel_instruccion.xlsx                       # Standardized educational attainment dataset
├── TRABAJO.xlsx                                 # Official historical labor survey time series (1999-2025)
├── Lara.xls                                     # Locality-level infrastructure and census microdata
├── Poblacion-*.xlsx                             # Baseline demographic data by age, sex, and birthplace
├── Servicios-Censo_2011.xlsx                    # Basic utility infrastructure coverage by parish
├── VIVIENDAS-HOGARES-Y-PERSONAS-CENSO-2011.xlsx # Housing, household, and individual census aggregates
└── README.md                                    # Technical, methodological, and legal documentation
```

---

## 4. Data Provenance & Citations
All datasets used in this research originate from official Venezuelan governmental statistics and international statistical bodies:

1. **National Institute of Statistics (INE - Instituto Nacional de Estadística), Bolivarian Republic of Venezuela:**
   * **XIV National Population and Housing Census (2011):** Aggregated census microdata processed via the *Redatam+SP* web server (UN-ECLAC/CELADE) and official published summary bulletins.
   * **Household Sample Survey (EHM - Encuesta de Hogares por Muestreo):** Global Labor Force Indicators, 1st Semesters 1999–2025 (employment status, formal/informal sectors, ISIC economic branches, and schooling).
   * **Vital Statistics:** Continuous civil registry series for births and marriages across states and municipalities.
2. **CELADE - Population Division of ECLAC (United Nations Economic Commission for Latin America and the Caribbean):**
   * Standards and computational methodologies of the *Redatam+SP* system (*Retrieval of Data for Small Areas by Microcomputer*).

---

## 5. Legal Framework, Academic Fair Use & Compliance

> [!IMPORTANT]
> ### Academic Research Statement
> This repository represents an independent academic, educational, and quantitative research study conducted as part of undergraduate demographic training at the **Universidad Central de Venezuela (UCV)**. It is created solely for educational purposes, quantitative modeling demonstration, and non-commercial analytical skill portfolio showcase.

### Compliance & Legal Disclaimers

1. **Statistical Secrecy & Privacy Protection:**
   In compliance with **Article 22 of the Venezuelan Public Statistical Function Act (Ley de la Función Pública de Estadística)**, this repository **DOES NOT contain, process, or expose any personal, nominative, or individually identifiable microdata**. All data points are anonymized macro-level statistical aggregations released to the public domain by the official statistical bureau.
2. **Fair Use & Copyright Exemption:**
   In accordance with **Article 44 of the Venezuelan Copyright Law (Ley sobre el Derecho de Autor)** and international intellectual property conventions (Berne Convention), the use, transformation, and pedagogical analysis of public government statistics for strictly scientific, academic, and non-commercial research is fully lawful and protected.
3. **Non-Affiliation & Disclaimer of Official Endorsement:**
   This project is an independent computational analysis by academic researchers and **does not constitute an official report, endorsement, or certified statement** from the National Institute of Statistics (INE), the Government of Venezuela, or UN-ECLAC. Neither the author nor associated academic entities assume liability for secondary interpretations or derivative usage by third parties.
4. **Code License:**
   The parsing code, ETL pipelines, and quantitative algorithms are distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.
