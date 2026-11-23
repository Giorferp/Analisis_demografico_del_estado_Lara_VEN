# ESPECIFICACIÓN TÉCNICA DE ESTANDARIZACIÓN Y NOMENCLATURA OFICIAL — PROYECTO ESTADO LARA (CENSO 2011)

**Autor Oficial del Estudio:** Giovanni (C.I. 31.126.857)  
**Institución:** Universidad Central de Venezuela (UCV) — Facultad de Ciencias Económicas y Sociales (FACES) — Escuela de Estadística y Ciencias Actuariales (EECA)  
**Cátedra:** Demografía (Prof. Isbelia Lugo)  
**Entidad Federal bajo Estudio:** Estado Lara y sus nueve (9) municipios autónomos (*Iribarren, Torres, Palavecino, Jiménez, Morán, Crespo, Andrés Eloy Blanco, Simón Planas y Urdaneta*), en contraste sistemático con el agregado nacional de la **República Bolivariana de Venezuela** (XIV Censo Nacional de Población y Vivienda 2011).  
**Stack de Procesamiento y Compilación:** Entorno Python gestionado con `uv`, base de datos relacional analítica `demografia_lara.db` (SQLite) y manuscrito en Jupyter Notebook (`.ipynb`) compilado directamente a PDF vía $\text{LaTeX}$ (`nbconvert --to pdf --no-input`), ocultando el código fuente crudo en el documento final.

---

## 1. GLOSARIO DE TÉRMINOS OBLIGATORIOS Y MAPEO CANÓNICO (INE / CEPAL / UCV)

Todo agente redactor, programador o auditor del estudio del **Estado Lara** debe emplear exclusivamente el **Término Obligatorio** y la **Notación Exacta** registrados en la siguiente matriz. El uso de cualquiera de los términos listados en la columna **Sinónimos Prohibidos** constituye una violación crítica de estandarización.

### 1.1. Matriz de Mapeo Terminológico y Notacional

| Concepto | Término Obligatorio | Sinónimos Prohibidos | Notación Exacta |
| :--- | :--- | :--- | :--- |
| Efectivo poblacional total en el instante censal $t$ | Población Total Censada | Habitantes totales, masa demográfica, volumen de gente, universo ciudadano | $N_t$ |
| Efectivo poblacional en el intervalo etario $[x, x+n)$ | Población por Grupo de Edad | Cohorte quinquenal (incorrecto en corte transversal), segmento etario, tramo de edad | $N_{(x,n)}$ |
| Proporción de niños y adolescentes ($0\text{–}14\text{ años}$) sobre el total | Índice de Juventud | Tasa de juventud, porcentaje infantil, cuota de menores | $\text{IJ}$ |
| Proporción de adultos mayores ($65\text{ años y más}$) sobre el total | Índice de Vejez | Tasa de ancianidad, porcentaje senil, cuota de tercera edad | $\text{IV}$ |
| Edad que divide exactamente en dos partes iguales la distribución poblacional | Edad Mediana | Edad promedio, media de edad, punto medio etario | $Me$ |
| Relación entre población potencialmente inactiva ($<15$ y $65+$) y activa ($15\text{–}64$) | Razón de Dependencia Demográfica Total | Tasa de dependencia, carga poblacional, índice de parasitismo demográfico | $\text{RDD}$ |
| Relación entre población menor de $15\text{ años}$ y población de $15\text{–}64\text{ años}$ | Razón de Dependencia Infantil | Tasa de dependencia juvenil, carga de menores, dependencia de niños | $\text{RDI}$ |
| Relación entre población de $65\text{ años y más}$ y población de $15\text{–}64\text{ años}$ | Razón de Dependencia Envejecida | Dependencia de ancianos, tasa de carga senil, dependencia de tercera edad | $\text{RDE}$ |
| Relación entre adultos mayores ($65+$) y menores de $15\text{ años}$ por cien | Índice de Envejecimiento | Razón abuelos-nietos, tasa de envejecimiento, índice de senectud | $\text{I. ENV}$ |
| Relación entre el efectivo de hombres y el de mujeres por cien | Índice de Masculinidad | Razón de sexos, tasa de masculinidad, proporción de varones | $\text{IM}$ ; $\text{IM}_{(x,n)}$ |
| Condición de saber leer y escribir un párrafo simple en población de $10\text{ años y más}$ | Condición de Alfabetismo | Grado de alfabetización, escolaridad básica, cultura letrada | $\text{TAnalf}$ |
| Máximo grado o año de estudio aprobado en el sistema educativo formal ($5\text{ años y más}$) | Nivel de Instrucción | Grado académico, escolaridad alcanzada, estatus educacional | $\% \text{Nivel}_k$ |
| Estado civil o de convivencia de hecho de las personas de $15\text{ años y más}$ | Situación Conyugal | Estado civil legal, estatus matrimonial, condición de pareja | $\% \text{Casados y Unidos}$ ; $\% \text{Solteros}$ ; $\% \text{VSD}$ |
| Población de $15\text{ años y más}$ con edad legal para participar en el mercado laboral | Población en Edad de Trabajar | Población adulta laboral, fuerza potencial, capital humano activo | $N_{\text{PET}}$ ($N_{15+}$) |
| Personas de $15\text{ años y más}$ ocupadas o que buscan trabajo activamente | Población Económicamente Activa | Fuerza laboral, masa trabajadora, oferta de mano de obra | $\text{PEA}$ |
| Personas de $15\text{ años y más}$ que no trabajan ni buscan empleo (estudiantes, hogar, rentistas) | Población No Económicamente Activa | Población inactiva, desempleados voluntarios, población pasiva | $\text{PNEA}$ |
| Personas en la $\text{PEA}$ con empleo remunerado o ayudantes familiares no remunerados | Población Ocupada | Empleados totales, trabajadores con puesto, población colocada | $\text{PO}$ |
| Personas en la $\text{PEA}$ sin empleo que buscan trabajo (Cesantes y BTPV) | Población Desocupada | Parados, desempleados totales, vagos, sin oficio | $\text{PD}$ |
| Relación porcentual entre la $\text{PEA}$ y la población total $N_t$ | Tasa Bruta de Actividad Económica | Tasa general de empleo, porcentaje de trabajadores, índice laboral bruto | $\text{TBAE}$ |
| Relación porcentual entre la $\text{PEA}$ y la población de $15\text{ años y más}$ ($N_{15+}$) | Tasa de Actividad Económica | Tasa de participación laboral, tasa refinada de empleo, índice de actividad | $\text{TAE}$ ; $\text{TAE}_{(x,n)}^s$ |
| Relación porcentual entre la $\text{PNEA}$ y la población de $15\text{ años y más}$ | Tasa de Inactividad Económica | Tasa de ocio, porcentaje de inactivos, tasa de no participación | $\text{TI}$ ; $\text{TBIE}$ |
| Relación porcentual entre la población desocupada ($\text{PD}$) y la $\text{PEA}$ | Tasa de Desocupación | Tasa de paro, índice de desempleo, porcentaje de cesantía | $\text{TD}$ |
| Relación entre inactivos más menores de $15\text{ años}$ respecto a la $\text{PEA}$ | Relación de Dependencia Económica | Carga económica real, razón de sostén económico, dependencia laboral | $\text{RDE}_{\text{econ}}$ |
| Segmentación de ocupados según tamaño del establecimiento ($<5$ trabajadores) y categoría | Sector Formal e Informal | Economía sumergida, empleo en negro, buhonería, economía subterránea | $\% \text{PO}_{\text{Formal}}$ ; $\% \text{PO}_{\text{Informal}}$ |
| Nacimientos vivos registrados por cada mil habitantes de la población media | Tasa Bruta de Natalidad | Índice de nacimientos, tasa de natalidad general, frecuencia de partos | $\text{TBN}$ |
| Nacimientos vivos por cada mil mujeres en edad fértil ($15\text{–}49\text{ años}$) | Tasa de Fecundidad General | Tasa global de maternidad, fecundidad femenina total, índice fértil | $\text{TFG}$ |
| Frecuencia de nacimientos vivos por edad quinquenal de la madre sobre mujeres de esa edad | Tasas Específicas de Fecundidad por Edad | Tasas de maternidad por tramo, fertilidad por grupo etario, curva fértil | $f_{(x,5)}$ |
| Número medio de hijos por mujer al término de su vida fértil bajo fecundidad transversal $f_{(x,5)}$ | Tasa Global de Fecundidad | Índice sintético de fecundidad, promedio de hijos por madre, tasa total de fertilidad | $\text{TGF}$ |
| Número medio de hijas mujeres que reemplazarían a cada madre en ausencia de mortalidad | Tasa Bruta de Reproducción | Tasa de reemplazo materno, índice de reproducción femenina, cuota de hijas | $R'$ |
| Promedio acumulado de hijos nacidos vivos tenidos por mujer según grupo de edad ($12+$) | Paridez Media Acumulada | Promedio histórico de hijos, fecundidad acumulada, tamaño familiar medio | $P_{(x,5)}$ |
| Proporción de mujeres declarantes con cero hijos nacidos vivos en el grupo de edad | Porcentaje de Nuliparidad | Tasa de infertilidad, porcentaje de mujeres sin descendencia, infecundidad | $\% \text{Nuliparidad}_{(x,5)}$ |
| Defunciones totales registradas por cada mil habitantes | Tasa Bruta de Mortalidad | Tasa general de muerte, índice de letalidad poblacional, frecuencia de óbitos | $\text{TBM}$ ($d$) |
| Frecuencia de defunciones en el grupo $[x, x+n)$ respecto a la población media de ese mismo grupo | Tasas Específicas de Mortalidad por Edad | Mortalidad por tramo, riesgo etario de muerte, letalidad por edad | ${}_nM_x$ |
| Defunciones de menores de un año por cada mil nacidos vivos registrados | Tasa de Mortalidad Infantil | Mortalidad de niños, letalidad pediátrica, tasa de óbitos infantiles | $\text{TMI}$ |
| Defunciones ocurridas en los primeros $27\text{ días}$ ($<28\text{ días}$) por cada mil nacidos vivos | Tasa de Mortalidad Neonatal | Mortalidad de recién nacidos, mortalidad perinatal temprana, letalidad neonatal | $\text{TMN}$ |
| Defunciones ocurridas entre los $28\text{ días}$ y los $11\text{ meses}$ cumplidos por mil nacidos vivos | Tasa de Mortalidad Postneonatal | Mortalidad infantil tardía, mortalidad exógena pediátrica | $\text{TMP}$ |
| Defunciones por causas obstétricas (embarazo, parto y puerperio) por cien mil nacidos vivos | Tasa de Mortalidad Materna | Razón de muerte materna, letalidad obstétrica, mortalidad de parturientas | $\text{TMM}$ |
| Tasa bruta recalculada aplicando tasas específicas observadas ${}_nM_x$ a una población estándar $N^t_{(x,n)}$ | Tasa Bruta de Mortalidad Tipificada | Tasa ajustada por edad, mortalidad estandarizada, tasa corregida | $d^t$ |
| Individuos cuya entidad de residencia habitual coincide con su entidad de nacimiento/origen previo | No Migrantes | Población sedentaria, residentes fijos, autóctonos permanentes | $NM_i$ |
| Individuos residentes en el Estado Lara nacidos (o residentes hace 5 años) en otra entidad federal | Inmigrantes Internos | Foráneos estatales, recién llegados internos, población alóctona | $I_i$ |
| Individuos nacidos (o residentes hace 5 años) en el Estado Lara censados en otra entidad federal | Emigrantes Internos | Desplazados hacia otros estados, diáspora larense interna, salientes | $E_i$ |
| Diferencia algebraica entre inmigrantes y emigrantes internos ($I_i - E_i$) | Saldo Migratorio Neto | Balance migratorio, ganancia/pérdida poblacional neta, flujo neto | $\text{SMN}$ |
| Suma total de movimientos de entrada y salida migratoria ($I_i + E_i$) | Saldo Migratorio Bruto | Volumen migratorio total, rotación espacial bruta, tráfico migratorio | $\text{SMB}$ |
| Fracción media del primer año de vida vivida por quienes fallecen antes de cumplir $1\text{ año}$ | Factor de Separación Infantil | Constante de Reed-Merrell infantil, ponderador neonatal, fracción de año $a_0$ | $f_0$ |
| Probabilidad de que un sobreviviente de edad exacta $x$ fallezca antes de alcanzar la edad $x+n$ | Probabilidad de Muerte entre $x$ y $x+n$ | Riesgo de muerte del intervalo, tasa actuarial de fallecimiento | ${}_nq_x$ |
| Número de personas de la cohorte hipotética inicial ($l_0 = 100.000$) que alcanzan con vida la edad exacta $x$ | Sobrevivientes a la Edad Exacta $x$ | Población viva a la edad $x$, efectivos supervivientes, curva de vida | $l_x$ |
| Años-persona vividos por la cohorte estacionaria entre las edades exactas $x$ y $x+n$ | Población Estacionaria del Intervalo | Tiempo vivido grupal, efectivos medios estacionarios | ${}_nL_x$ |
| Relación de supervivencia entre dos grupos quinquenales consecutivos de población estacionaria | Relación de Supervivencia Quinquenal | Probabilidad de paso quinquenal, factor de sobrevivencia censal | ${}_5P_x$ ; $P_b$ |
| Total de años-persona por vivir acumulados por la cohorte desde la edad exacta $x$ hasta $\omega$ | Total de Años-Persona por Vivir desde $x$ | Masa remanente de vida, años futuros acumulados | $T_x$ |
| Número medio de años adicionales de vida esperados para un sobreviviente de edad exacta $x$ | Esperanza de Vida a la Edad $x$ | Expectativa de vida, longevidad media restante, vida probable | $e_x^0$ |

### 1.2. Definiciones Contextuales Operativas (Estándar INE / CEPAL / UCV)

1. **Criterio de Empadronamiento (*De Jure* o Derecho):** El XIV Censo Nacional de Población y Vivienda 2011 contabiliza a las personas en su **lugar de residencia habitual** (municipio y entidad donde viven permanentemente o tienen intención de permanecer al menos seis meses), independientemente de dónde se encontraban la noche censal.
2. **Clasificación Etaria Estructural de la Cátedra de Demografía:** Toda evaluación del estadio transicional del Estado Lara debe contrastar el Índice de Juventud ($\text{IJ}$) y el Índice de Vejez ($\text{IV}$) contra los umbrales normativos de la cátedra:
   - **Población Joven:** $\text{IJ} \in [40\%, 50\%]$ (o $>35\%$) e $\text{IV} < 4\%$.
   - **Población Adulta (en Transición):** $\text{IJ} \in [30\%, 40\%]$ e $\text{IV} \in [4\%, 5\%]$.
   - **Población Envejecida / Vieja:** $\text{IJ} < 30\%$ e $\text{IV} \ge 6\%$.
3. **Fuerza de Trabajo y Sector Informal:** La Población Económicamente Activa ($\text{PEA}$) en el corte 2011 comprende el universo de $15\text{ años y más}$ (homologando con $10\text{ años y más}$ solo cuando se contraste contra tabulados históricos del Censo 2001 que usen ese umbral, dejando constancia explícita en nota al pie). El **Sector Informal** agrupa a los trabajadores por cuenta propia no profesionales, patronos y empleados de microempresas ($<5$ trabajadores), ayudantes familiares no remunerados y servicio doméstico.
4. **Fecundidad Corregida ($B^*_{(x,5)}$):** Queda terminantemente prohibido excluir los nacimientos vivos con edad de la madre «No Declarada» o graficarlos como una categoría separada. Antes de calcular $\text{TBN}$, $\text{TFG}$, $f_{(x,5)}$, $\text{TGF}$ y $R'$, debe ejecutarse la **redistribución proporcional** sobre los siete grupos quinquenales fértiles ($15\text{–}19$ a $45\text{–}49\text{ años}$):
   $$B^*_{(x,5)} = B^{\text{obs}}_{(x,5)} + B_{\text{No Decl.}} \times \left( \frac{B^{\text{obs}}_{(x,5)}}{\sum_{i=15}^{45} B^{\text{obs}}_{(i,5)}} \right)$$

---

## 2. CONVENCIONES DE NOTACIÓN, SIMBOLOGÍA Y RIGOR MATEMÁTICO

### 2.1. Sistema de Subíndices y Superíndices (Estándar Técnico Lara)
- **Subíndice temporal $t$ o $z$:** Identifica el año calendario o corte censal ($t \in \{1981, 1990, 2001, 2011, 2016\}$). Ejemplo: $N_{2011}$, $\text{TBN}_{2011}$.
- **Subíndice de intervalo de edad $(x,n)$ o prefijo inferior $n$ y sufijo inferior $x$:**
  - En efectivos poblacionales, razones de masculinidad y tasas de fecundidad se utiliza la notación parentética postfija: $N_{(x,5)}$, $\text{IM}_{(x,5)}$, $f_{(x,5)}$.
  - En funciones biométricas de mortalidad y tablas de vida se utiliza la notación actuarial clásica con prefijo de amplitud $n$ y sufijo de edad exacta $x$: ${}_nM_x$, ${}_nq_x$, ${}_np_x$, ${}_nd_x$, ${}_nL_x$, ${}_5P_x$.
- **Superíndice de sexo $s \in \{H, M\}$:** Identifica Hombres ($H$) y Mujeres ($M$). Ejemplo: $N_{(x,5)}^H$, $N_{(x,5)}^M$, $e_0^{0,H}$, $e_0^{0,M}$.
- **Superíndice de tipificación $t$:** Identifica magnitudes estandarizadas por estructura etaria: $N^t_{(x,n)}$ (población estándar media), $D^t$ (defunciones esperadas), $d^t$ (tasa bruta de mortalidad tipificada).

### 2.2. Reglas de Escala, Unidades de Medida y Redondeo (Norma Venezolana)
1. **Separadores Numéricos:** Se aplica sin excepción la convención hispano-venezolana oficial del INE: **punto (`.`) para separar miles** y **coma (`,`) para separar decimales** (ejemplo: $1.774.867\text{ habitantes}$; $\text{TGF} = 2,38\text{ hijos por mujer}$; ${}_5q_{20} = 0,008412$).
2. **Unidades de Expresión por Familia de Indicadores:**
   - **Porcentajes ($\%$, base $100$):** Pesos relativos poblacionales ($\% N_{(x,n)}$), $\text{IJ}$, $\text{IV}$, tasas educativas ($\text{TAnalf}$, $\% \text{Nivel}_k$), indicadores de situación conyugal ($\% \text{Casados y Unidos}$, $\% \text{Solteros}$, $\% \text{VSD}$), tasas laborales ($\text{TBAE}$, $\text{TAE}$, $\text{TBIE}$, $\text{TI}$, $\text{TD}$) y porcentaje de nuliparidad. Precisión obligatoria: **dos (2) decimales** (ej. $66,42\%$).
   - **Razones por Cien Personas (adimensionales base $100$, sin símbolo $\%$ en la definición conceptual aunque se expresen por cada $100$):** $\text{RDD}$, $\text{RDI}$, $\text{RDE}$, $\text{I. ENV}$, $\text{IM}$, $\text{IM}_{(x,n)}$ y $\text{RDE}_{\text{econ}}$. Precisión obligatoria: **dos (2) decimales** en tablas de cálculo y **redondeo al entero más próximo** en la frase de traducción operativa (ej. `"por cada 100 mujeres había aproximadamente 98 hombres"`).
   - **Tasas por Mil ($\text{‰}$, base $1.000$):** $\text{TBN}$, $\text{TFG}$, $\text{TBM}$ ($d$), tasa tipificada ($d^t$), $\text{TMI}$, $\text{TMN}$, $\text{TMP}$ y Tasa de Migración Neta Anual ($\text{TMN}_{\text{mig}}$). Precisión obligatoria: **dos (2) decimales** (ej. $18,45\text{‰}$).
   - **Tasas por Cien Mil (base $100.000$):** Tasa de Mortalidad Materna ($\text{TMM}$) y raíz de la tabla abreviada de mortalidad ($l_0 = 100.000$).
   - **Funciones de Tabla de Vida y Tasas en Tanto por Uno:** Tasas específicas ${}_nM_x$ (en tablas de vida y tipificación), probabilidades ${}_nq_x$, ${}_np_x$, relaciones de supervivencia ${}_5P_x$, $P_b$ y factor $f_0$ se reportan con **seis (6) decimales** ($0,000000$). Los efectivos $l_x$, ${}_nd_x$, ${}_nL_x$ y $T_x$ se expresan como **enteros separando miles con punto**, y la esperanza de vida $e_x^0$ con **dos (2) decimales** en años.
3. **Tratamiento de Anglicismos y Siglas:** Queda prohibido el uso de anglicismos no traducidos (*stock*, *gap*, *ratio*, *cluster*, *baby boom*, *commuting*). Se emplearán sus equivalentes canónicos en español: *efectivo censal*, *brecha*, *razón*, *conglomerado territorial*, *auge natalista*, *movilidad pendular laboral*. Las siglas institucionales y demográficas ($\text{INE}$, $\text{CEPAL}$, $\text{CELADE}$, $\text{MPPS}$, $\text{PEA}$, $\text{PNEA}$, $\text{BTPV}$) se declaran completas en su primera aparición y posteriormente se usan sin puntos intermedios.

### 2.3. Salvaguardas Matemáticas Anti-Errores del Corpus Histórico
1. **Amplitud Exacta en la Edad Mediana ($Me$):** En el cálculo de $Me = L_i + \left(\frac{N_t/2 - F_{i-1}}{f_i}\right) \cdot A_i$, para grupos quinquenales de edades cumplidas ($0\text{–}4, 5\text{–}9, \dots$), la amplitud del intervalo continuo $[x, x+5)$ es **estrictamente $A_i = 5$** (jamás $4$).
2. **Denominador de Tasas Específicas de Mortalidad (${}_nM_x$):** Cada tasa específica ${}_nM_x = \frac{D_{(x,n)}}{N_{(x,n)}}$ divide las defunciones del grupo etario entre el **efectivo poblacional de ese mismo grupo de edad $N_{(x,n)}$** (y del mismo sexo cuando se desagrega por sexo), verificando computacionalmente que $\sum_x {}_nM_x \cdot N_{(x,n)} = D_{\text{total}}$.
3. **Cierre del Grupo Abierto Final ($\omega$) en Tablas de Vida:** Para el grupo abierto final ($x = \omega$), se impone ${}_\infty q_\omega = 1,000000$, ${}_\infty d_\omega = l_\omega$ y ${}_\infty L_\omega = T_\omega = \frac{l_\omega}{{}_\infty M_\omega}$.

---

## 3. REGLAS DE ESTILO, FORMATO VISUAL Y ARQUITECTURA DOCUMENTAL (IDENTIDAD LARA)

### 3.1. Voz Gramatical, Sintaxis y Umbral Epistemológico
1. **Voz Gramatical y Tiempos Verbales:** Redacción estricta en **tercera persona impersonal con pasiva refleja** (*"se observa"*, *"se cuantifica"*, *"se registra"*, *"se determina"*). Queda prohibida la primera persona del singular o plural (*"calculamos"*, *"nuestro análisis"*). Los hallazgos de los cortes censales 1981–2011 se redactan en **pretérito perfecto simple** o **presente histórico analítico**, y el comportamiento matemático de funciones e identidades en **presente atemporal**.
2. **Mecánica de Prosa y Densidad:** Párrafos analíticos de alta densidad informativa ($110\text{ a }180\text{ palabras}$ en promedio) con asimetría deliberada en la longitud oracional (*burstiness*: alternancia de oraciones fácticas cortas de $5\text{–}8\text{ palabras}$ seguidas de períodos subordinados causales). Apertura y cierre en frío en cada apartado.
3. **Doble Nivel de Lectura Obligatorio:** Todo cuadro o gráfico debe ir sucedido de:
   - **Nivel 1 (Traducción Operativa):** Frase canónica obligatoria en personas enteras redondeadas (*"Para el año 2011, en el Estado Lara, por cada 100 personas en edad potencialmente activa (15–64 años) dependían aproximadamente X menores de 15 años y Y adultos mayores de 65 años y más"*).
   - **Nivel 2 (Mecanismo Causal Sociodemográfico):** Explicación del *por qué* empírico vinculando la métrica con la estructura territorial larense, la transición demográfica, los diferenciales de género o la transición epidemiológica.
4. **Umbral Epistemológico:** El documento incluye una subsección preliminar de **Conceptos Básicos Operativos** exigida por la cátedra. Fuera de dicha subsección, **queda prohibido re-explicar pedagógicamente qué es una mediana, qué es una tasa bruta o cómo se lee una pirámide**; el texto en los capítulos analíticos debe entrar directamente al diferencial numérico entre el Estado Lara, sus municipios y Venezuela.

### 3.2. Maquetación Tipográfica y Numeración Seccional (Estándar Decimal Técnico)
- **Tipografía del Manuscrito PDF ($\text{LaTeX}$):** Familia **Sans-Serif Técnica Moderna / Charter** (`\usepackage{lmodern}` con títulos en Sans-Serif `\sffamily\bfseries` en color Azul Marino `#1B365D`, o combinación `helvet` / `charter`), interlineado $1,15$, márgenes de $2,5\text{ cm}$ y texto justificado sin sangría francesa, con espaciado entre párrafos (`\parskip=6pt`).
- **Jerarquía de Encabezados (Numeración Decimal Pura):** Se prohíbe el uso de números romanos en títulos de capítulos (reservado exclusivamente a otra línea editorial). En el informe del **Estado Lara** se emplea numeración arábiga decimal técnica con sustantivos secos y precisos:
  - `1. CONTEXTO GEO-HISTÓRICO Y ESTRUCTURA POBLACIONAL POR EDAD Y SEXO`
  - `1.1. Evolución Intercensal del Volumen Poblacional (1981–2011)`
  - `1.1.1. Distribución Espacial por Ejes Funcionales y Municipios`
  - `2. CARACTERÍSTICAS EDUCATIVAS DE LA POBLACIÓN`
  - `3. SITUACIÓN CONYUGAL Y NUPCIALIDAD`
  - `4. FUERZA DE TRABAJO Y ESTRUCTURA ECONÓMICA`
  - `5. DINÁMICA DEMOGRÁFICA: FECUNDIDAD, MORTALIDAD Y MIGRACIÓN`
  - `6. TABLAS ABREVIADAS DE MORTALIDAD Y PROYECCIONES DEMOGRÁFICAS (2011–2016)`
  - `7. SÍNTESIS ANALÍTICA Y REFERENCIAS BIBLIOGRÁFICAS`

### 3.3. Diseño Visual de Tablas (`Cuadro X.Y` — Estilo *Booktabs* Minimalista)
1. **Rotulación Oficial:** Todas las tablas deben titularse exclusivamente como **`Cuadro X.Y`** (donde `X` es el número arábigo de la sección principal e `Y` el correlativo dentro de la sección: `Cuadro 1.1`, `Cuadro 1.2`, ..., `Cuadro 6.4`). **Queda prohibido el uso de la palabra `Tabla` en el estudio del Estado Lara.**
2. **Estructura del Título:** Ubicado en la parte superior, alineado a la izquierda, en negrita el rótulo (`Cuadro 1.1.`) y en redonda el título descriptivo completo: **Estado Lara: [Universo/Variable], según [Variable de fila] por [Variable de columna], [Año(s)]**.
3. **Estética *Booktabs*:**
   - **Cero líneas verticales** y cero rejillas internas cerradas.
   - Tres líneas horizontales de calibre diferenciado: `\toprule` superior ($1,2\text{ pt}$ en `#1B365D`), `\midrule` bajo el encabezado de columnas ($0,6\text{ pt}$) y `\bottomrule` al cierre del cuadro ($1,2\text{ pt}$), más una línea fina (`\cmidrule`) antes de la fila de **Total**.
   - Fondo completamente blanco o con sombreado gris hielo ultra-tenue (`#F2F5F8`) exclusivamente en la fila de encabezados y en la fila `Total`.
   - Cierre obligatorio al pie en tamaño `8pt`: `Fuente: Instituto Nacional de Estadística (INE), XIV Censo Nacional de Población y Vivienda 2011. Cálculos propios.`

### 3.4. Estándar Gráfico (`matplotlib` / `seaborn` — Paleta Fría Institucional)
Todos los gráficos del informe de Lara se generan programáticamente en Python (`dpi=300`, formato vectorial PDF/PNG de alta resolución) bajo una identidad visual fría, sobria y corporativa:
1. **Paleta Cromática Oficial (Hexadecimal):**
   - **Serie Primaria / Hombres / Año 2011 / Estado Lara:** Azul Marino Institucional `#1B365D`.
   - **Serie Secundaria / Año 2001 / Comparativa Nacional (Venezuela):** Gris Pizarra `#4A607A`.
   - **Serie Terciaria / Grupos Intermedios / Sector Formal:** Acero Azulado `#7BA0C0`.
   - **Contraste de Sexo (Mujeres) / Alertas Epidemiológicas (Sobremortalidad / Sector Informal):** Coral Sobrio `#C0392B`.
   - **Series Auxiliares (Niveles Educativos / Ramas Económicas):** Gradiente secuencial frío `['#1B365D', '#2E5B88', '#4A7C59', '#7BA0C0', '#A3B8CC', '#C0392B']`.
2. **Geometría y Limpieza del Lienzo (`rcParams`):**
   - Desactivación de bordes superior y derecho (`sns.despine(top=True, right=True)`).
   - Grillas exclusivamente horizontales (o verticales en pirámides y barras horizontales), punteadas (`linestyle='--'`), color `#B0BEC5` con opacidad `alpha=0.25`.
   - **Leyendas:** Ubicadas en la **esquina superior derecha** (`loc='upper right'`, `frameon=False`) o integradas mediante etiquetas directas al final de cada curva. Prohibido colocar leyendas en la parte inferior con caja cerrada.
   - Rótulo inferior o superior numerado como **`Gráfico X.Y.`** (ej. `Gráfico 1.1. Estado Lara: Pirámide de población por grupos quinquenales de edad y sexo, 2001–2011 (%)`).

### 3.5. Reglas de Contraste Nacional (Venezuela) y Desagregación Municipal (9 Municipios)
1. **Contraste Sistemático contra la República Bolivariana de Venezuela:** En cada bloque temático, los indicadores del Estado Lara deben contrastarse contra el valor homólogo nacional del Censo 2011 (peso demográfico y territorial de Lara en Venezuela, comparación de $\text{IJ}$, $\text{IV}$, $Me$, $\text{RDD}$, $\text{IM}$, $\text{TAnalf}$, $\text{TAE}$, $\text{TD}$, $\text{TBN}$, $\text{TGF}$, $\text{TBM}$, curvas ${}_nM_x$, **Tipificación Directa de Mortalidad Estado Lara vs. Venezuela**, y matriz migratoria inter-estatal $24 \times 24$).
2. **Desagregación obligatoria en los 9 Municipios Autónomos de Lara:**
   - Todo análisis territorial y de condición de actividad económica debe desglosar explícitamente los **9 municipios**: **Iribarren** (capital Barquisimeto), **Palavecino** (Cabudare), **Torres** (Carora), **Jiménez** (Quíbor), **Morán** (El Tocuyo), **Crespo** (Duaca), **Andrés Eloy Blanco** (Sanare), **Simón Planas** (Sarare) y **Urdaneta** (Siquisique).
   - La interpretación causal debe explicar la **macrocefalia metropolitana del eje conurbado Barquisimeto–Cabudare** (municipios Iribarren y Palavecino, que concentran el sector terciario moderno, la matrícula universitaria, la inmigración interna y las menores tasas de dependencia infantil), en contraposición con el eje agroindustrial y semiárido occidental (**Torres** y **Urdaneta**) y el cinturón agrícola andino-larense (**Morán**, **Jiménez**, **Andrés Eloy Blanco**, **Crespo** y **Simón Planas**), caracterizados por mayor índice de masculinidad rural ($\text{IM} > 105$ por emigración selectiva femenina hacia Barquisimeto), menor inserción formal y envejecimiento relativo por éxodo juvenil.

---

## 4. LISTA DE VERIFICACIÓN DE CUMPLIMIENTO (CHECKLIST DE AUDITORÍA)

Antes de dar por válido cualquier capítulo o entregable del proyecto **Estado Lara**, el agente redactor y el auditor causal deben verificar que se cumplan el $100\%$ de los siguientes puntos:

- [ ] **1. Autoría e Identidad:** ¿Figura exclusivamente **Giovanni (C.I. 31.126.857)** como autor en la portada institucional UCV/FACES/EECA (Cátedra Demografía, Prof. Isbelia Lugo) y se omitió todo rastro de código fuente Python en el PDF compilado?
- [ ] **2. Barrera China Editorial:** ¿Están todos los capítulos numerados en sistema arábigo decimal (`1.`, `1.1.`, `1.1.1.`), todas las tablas rotuladas como **`Cuadro X.Y`** (cero apariciones de la palabra `Tabla`) con formato *booktabs* sin bordes verticales, y todos los gráficos generados en `matplotlib`/`seaborn` con la paleta fría `#1B365D` / `#4A607A` / `#7BA0C0` / `#C0392B` y leyenda superior sin marco?
- [ ] **3. Pureza Terminológica:** ¿Se respetaron estrictamente los términos obligatorios del Glosario (Sección 1.1) sin incurrir en ningún sinónimo prohibido ni en palabras de la lista negra léxica (*crucial, fascinante, tapiz, catalizador, desentrañar, panorama, robusto, en resumen, cabe señalar*)?
- [ ] **4. Formato Numérico Venezolano:** ¿Todos los números del texto, cuadros y ejes gráficos utilizan punto (`.`) para miles y coma (`,`) para decimales, respetando las unidades (`%`, `‰`, `por 100.000`) y la cantidad exacta de decimales (2 en tasas/porcentajes, 6 en funciones biométricas ${}_nM_x, {}_nq_x, {}_5P_x$)?
- [ ] **5. Exactitud Matemática en Fórmulas Críticas:**
  - ¿Se usó $A_i = 5$ en el cálculo de la Edad Mediana ($Me$)?
  - ¿Se redistribuyeron proporcionalmente los nacimientos con edad de la madre no declarada ($B^*_{(x,5)}$) antes de calcular $f_{(x,5)}$, $\text{TGF}$ y $R'$?
  - ¿Se dividieron las defunciones $D_{(x,n)}$ entre el efectivo del mismo grupo etario $N_{(x,n)}$ para obtener ${}_nM_x$?
  - ¿Se construyó la matriz de **Tipificación Directa** con Diferencias Horizontales ($d - d^t$) y Diferencias Verticales, y se calcularon las tres Tablas Abreviadas de Mortalidad (Total, Hombres, Mujeres) con su respectivo factor de separación $f_0$?
- [ ] **6. Cobertura de los 9 Municipios y Contraste con Venezuela:** ¿Incluye el estudio la desagregación completa para *Iribarren, Torres, Palavecino, Jiménez, Morán, Crespo, Andrés Eloy Blanco, Simón Planas y Urdaneta*, y el contraste sistemático de los indicadores estadales frente al total de la República Bolivariana de Venezuela?
- [ ] **7. Doble Nivel Interpretativo y Rigor Causal:** ¿Cada cuadro y gráfico va acompañado de la traducción operativa estandarizada (*"Por cada 100 / 1.000..."*) y de una explicación causal completa (mecanismo sociodemográfico/epidemiológico + implicación estructural) sin párrafos de relleno?
