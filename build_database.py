import os
import re
import sqlite3
import unicodedata
import pandas as pd
import numpy as np

DB_PATH = "demografia_lara.db"

def clean_col(col_name: str) -> str:
    """Normaliza nombres de columna a snake_case ASCII limpio."""
    c = str(col_name).strip().lower()
    c = c.replace("%", "pct_")
    c = unicodedata.normalize("NFKD", c).encode("ascii", "ignore").decode("ascii")
    c = re.sub(r"[^\w\s]", "", c)
    c = re.sub(r"\s+", "_", c)
    return c.strip("_")

def build_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Base de datos previa eliminada: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    print("--- 1. Población por Sexo (Censo 2011) ---")
    # Parroquias
    df_pob_sexo = pd.read_excel("Poblacion-Sexo-Censo-2011.xlsx", header=2)
    df_pob_sexo = df_pob_sexo.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df_pob_sexo.columns = [str(c).strip() for c in df_pob_sexo.columns]
    df_pob_sexo = df_pob_sexo.loc[:, ~df_pob_sexo.columns.str.startswith("Unnamed")]
    df_pob_sexo = df_pob_sexo.dropna(subset=["Entidad Federal", "Código UBIGEO"]).reset_index(drop=True)
    df_pob_sexo = df_pob_sexo.rename(columns={
        "Código UBIGEO": "codigo_ubigeo",
        "Entidad Federal": "entidad",
        "Municipio": "municipio",
        "Parroquia": "parroquia",
        "Total": "total",
        "Hombre": "hombre",
        "Mujer": "mujer"
    })
    df_pob_sexo["censo"] = 2011
    df_pob_sexo["codigo_ubigeo"] = df_pob_sexo["codigo_ubigeo"].astype(str).str.zfill(6)
    for num_col in ["total", "hombre", "mujer"]:
        df_pob_sexo[num_col] = pd.to_numeric(df_pob_sexo[num_col], errors="coerce").fillna(0).astype(int)
    cols_order = ["censo", "codigo_ubigeo", "entidad", "municipio", "parroquia", "total", "hombre", "mujer"]
    df_pob_sexo[cols_order].to_sql("pob_sexo_parroquia", conn, if_exists="replace", index=False)

    # Entidades
    df_sexo_ent = pd.read_excel("Poblacion-Sexo-Censo-2011-1.xlsx", header=2)
    df_sexo_ent = df_sexo_ent.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df_sexo_ent.columns = [str(c).strip() for c in df_sexo_ent.columns]
    df_sexo_ent = df_sexo_ent.loc[:, ~df_sexo_ent.columns.str.startswith("Unnamed")]
    df_sexo_ent = df_sexo_ent.dropna(subset=["Entidad Federal"]).reset_index(drop=True)
    df_sexo_ent = df_sexo_ent[~df_sexo_ent["Entidad Federal"].str.startswith("Estado:")].reset_index(drop=True)
    df_sexo_ent = df_sexo_ent.rename(columns={
        "Código UBIGEO": "codigo_ubigeo",
        "Entidad Federal": "entidad",
        "Total": "total",
        "Hombre": "hombre",
        "Mujer": "mujer"
    })
    df_sexo_ent["censo"] = 2011
    df_sexo_ent["codigo_ubigeo"] = df_sexo_ent["codigo_ubigeo"].fillna("000000").astype(str)
    for num_col in ["total", "hombre", "mujer"]:
        df_sexo_ent[num_col] = pd.to_numeric(df_sexo_ent[num_col], errors="coerce").fillna(0).astype(int)
    df_sexo_ent[["censo", "codigo_ubigeo", "entidad", "total", "hombre", "mujer"]].to_sql("pob_sexo_entidad", conn, if_exists="replace", index=False)

    print("--- 2. Población por Grupos de Edad (Censo 2011) ---")
    age_cols_map = {
        "Menores de 4 años": "edad_0_4",
        "De 5 a 9 años": "edad_5_9",
        "De 10 a 14 años": "edad_10_14",
        "De 15 a 19 años": "edad_15_19",
        "De 20 a 24 años": "edad_20_24",
        "De 25 a 29 años": "edad_25_29",
        "De 30 a 34 años": "edad_30_34",
        "De 35 a 39 años": "edad_35_39",
        "De 40 a 44 años": "edad_40_44",
        "De 45 a 49 años": "edad_45_49",
        "De 50 a 54 años": "edad_50_54",
        "De 55 a 59 años": "edad_55_59",
        "De 60 a 64 años": "edad_60_64",
        "De 65 a 69 años": "edad_65_69",
        "De 70 a 74 años": "edad_70_74",
        "De 75 a 79 años": "edad_75_79",
        "De 80 a 84 años": "edad_80_84",
        "De 85 a 89 años": "edad_85_89",
        "De 90 a 94 años": "edad_90_94",
        "95 años y Más": "edad_95_mas",
        "Total": "total",
        "Código UBIGEO": "codigo_ubigeo",
        "Entidad Federal": "entidad",
        "Municipio": "municipio",
        "Parroquia": "parroquia"
    }

    df_pob_edad = pd.read_excel("Poblacion-Grupos-Edad-Censo-2011.xlsx", header=2)
    df_pob_edad = df_pob_edad.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df_pob_edad.columns = [str(c).strip() for c in df_pob_edad.columns]
    df_pob_edad = df_pob_edad.loc[:, ~df_pob_edad.columns.str.startswith("Unnamed")]
    df_pob_edad = df_pob_edad.dropna(subset=["Entidad Federal", "Código UBIGEO"]).reset_index(drop=True)
    df_pob_edad = df_pob_edad.rename(columns=age_cols_map)
    df_pob_edad["censo"] = 2011
    df_pob_edad["codigo_ubigeo"] = df_pob_edad["codigo_ubigeo"].astype(str).str.zfill(6)
    num_age_cols = [v for k, v in age_cols_map.items() if k not in ["Código UBIGEO", "Entidad Federal", "Municipio", "Parroquia"]]
    for col in num_age_cols:
        df_pob_edad[col] = pd.to_numeric(df_pob_edad[col], errors="coerce").fillna(0).astype(int)
    cols_edad_order = ["censo", "codigo_ubigeo", "entidad", "municipio", "parroquia"] + num_age_cols
    df_pob_edad[cols_edad_order].to_sql("pob_edad_parroquia", conn, if_exists="replace", index=False)

    # Entidades
    df_edad_ent = pd.read_excel("Poblacion-Grupos-Edad-Censo-2011-1.xlsx", header=2)
    df_edad_ent = df_edad_ent.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df_edad_ent.columns = [str(c).strip() for c in df_edad_ent.columns]
    df_edad_ent = df_edad_ent.loc[:, ~df_edad_ent.columns.str.startswith("Unnamed")]
    df_edad_ent = df_edad_ent.dropna(subset=["Entidad Federal"]).reset_index(drop=True)
    df_edad_ent = df_edad_ent[~df_edad_ent["Entidad Federal"].str.startswith("Estado:")].reset_index(drop=True)
    df_edad_ent = df_edad_ent.rename(columns=age_cols_map)
    df_edad_ent["censo"] = 2011
    df_edad_ent["codigo_ubigeo"] = df_edad_ent["codigo_ubigeo"].fillna("000000").astype(str)
    for col in num_age_cols:
        df_edad_ent[col] = pd.to_numeric(df_edad_ent[col], errors="coerce").fillna(0).astype(int)
    cols_ent_order = ["censo", "codigo_ubigeo", "entidad"] + num_age_cols
    df_edad_ent[cols_ent_order].to_sql("pob_edad_entidad", conn, if_exists="replace", index=False)

    print("--- 3. Lugar de Nacimiento (Censo 2011) ---")
    df_pob_nac = pd.read_excel("Poblacion-Nacida-en-Venezuela-Censo-2011.xlsx", header=2)
    df_pob_nac = df_pob_nac.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df_pob_nac.columns = [str(c).strip() for c in df_pob_nac.columns]
    df_pob_nac = df_pob_nac.loc[:, ~df_pob_nac.columns.str.startswith("Unnamed")]
    df_pob_nac = df_pob_nac.dropna(subset=["Entidad Federal", "Código UBIGEO"]).reset_index(drop=True)
    df_pob_nac = df_pob_nac.rename(columns={
        "Código UBIGEO": "codigo_ubigeo",
        "Entidad Federal": "entidad",
        "Municipio": "municipio",
        "Parroquia": "parroquia",
        "Total": "total",
        "Población que Nació en Venezuela": "nacido_venezuela",
        "Población que  No Nació en Venezuela": "nacido_exterior"
    })
    df_pob_nac["censo"] = 2011
    df_pob_nac["codigo_ubigeo"] = df_pob_nac["codigo_ubigeo"].astype(str).str.zfill(6)
    for col in ["total", "nacido_venezuela", "nacido_exterior"]:
        df_pob_nac[col] = pd.to_numeric(df_pob_nac[col], errors="coerce").fillna(0).astype(int)
    cols_nac_order = ["censo", "codigo_ubigeo", "entidad", "municipio", "parroquia", "total", "nacido_venezuela", "nacido_exterior"]
    df_pob_nac[cols_nac_order].to_sql("pob_nacimiento_parroquia", conn, if_exists="replace", index=False)

    print("--- 4. Alfabetismo (Estado Lara) ---")
    # Por edad
    df_alf_edad = pd.read_excel("alfabetismo.xlsx", sheet_name="Por_Edad")
    df_alf_edad = df_alf_edad.set_index("Condición").T.reset_index()
    df_alf_edad.columns = ["grupo_edad", "alfabeta", "analfabeta", "total"]
    df_alf_edad["censo"] = 2011
    for c in ["alfabeta", "analfabeta", "total"]:
        df_alf_edad[c] = pd.to_numeric(df_alf_edad[c], errors="coerce").fillna(0).astype(int)
    df_alf_edad[["censo", "grupo_edad", "alfabeta", "analfabeta", "total"]].to_sql("alfabetismo_edad", conn, if_exists="replace", index=False)

    # Por sexo
    df_alf_sexo = pd.read_excel("alfabetismo.xlsx", sheet_name="Por_Sexo")
    df_alf_sexo.columns = ["sexo", "alfabeta", "analfabeta", "total"]
    df_alf_sexo["censo"] = 2011
    for c in ["alfabeta", "analfabeta", "total"]:
        df_alf_sexo[c] = pd.to_numeric(df_alf_sexo[c], errors="coerce").fillna(0).astype(int)
    df_alf_sexo[["censo", "sexo", "alfabeta", "analfabeta", "total"]].to_sql("alfabetismo_sexo", conn, if_exists="replace", index=False)

    # Cruce edad y sexo
    df_alf_cruce = pd.read_excel("alfabetismo.xlsx", sheet_name="Por_Edad_y_Sexo")
    df_alf_cruce = df_alf_cruce.rename(columns={
        "Grupo de edad": "grupo_edad",
        "Hombre Alfabeta": "hombre_alfabeta",
        "Hombre Analfabeta": "hombre_analfabeta",
        "Hombre Total": "hombre_total",
        "Mujer Alfabeta": "mujer_alfabeta",
        "Mujer Analfabeta": "mujer_analfabeta",
        "Mujer Total": "mujer_total",
        "Total Alfabeta": "total_alfabeta",
        "Total Analfabeta": "total_analfabeta",
        "Total General": "total_general"
    })
    df_alf_cruce["censo"] = 2011
    for col in df_alf_cruce.columns:
        if col not in ["censo", "grupo_edad"]:
            df_alf_cruce[col] = pd.to_numeric(df_alf_cruce[col], errors="coerce").fillna(0).astype(int)
    cruce_cols = ["censo", "grupo_edad", "hombre_alfabeta", "hombre_analfabeta", "hombre_total", "mujer_alfabeta", "mujer_analfabeta", "mujer_total", "total_alfabeta", "total_analfabeta", "total_general"]
    df_alf_cruce[cruce_cols].to_sql("alfabetismo_cruce", conn, if_exists="replace", index=False)

    print("--- 5. Nivel de Instrucción (Estado Lara) ---")
    inst_cols_map = {
        "Grupo de edad": "grupo_edad",
        "Sexo": "sexo",
        "No sabe": "no_sabe",
        "Ninguno": "ninguno",
        "Inicial (Preescolar)": "inicial",
        "Primaria (1-6)": "primaria",
        "Secundaria (1-5),(6)": "secundaria",
        "Técnico Superior": "tecnico_superior",
        "Universitario": "universitario",
        "Total": "total"
    }

    df_inst_edad = pd.read_excel("nivel_instruccion.xlsx", sheet_name="Por_Edad").rename(columns=inst_cols_map)
    df_inst_edad["censo"] = 2011
    for col in df_inst_edad.columns:
        if col not in ["censo", "grupo_edad"]:
            df_inst_edad[col] = pd.to_numeric(df_inst_edad[col], errors="coerce").fillna(0).astype(int)
    df_inst_edad.to_sql("instruccion_edad", conn, if_exists="replace", index=False)

    df_inst_10 = pd.read_excel("nivel_instruccion.xlsx", sheet_name="Por_Edad_10_mas").rename(columns=inst_cols_map)
    df_inst_10["censo"] = 2011
    for col in df_inst_10.columns:
        if col not in ["censo", "grupo_edad"]:
            df_inst_10[col] = pd.to_numeric(df_inst_10[col], errors="coerce").fillna(0).astype(int)
    df_inst_10.to_sql("instruccion_edad_10mas", conn, if_exists="replace", index=False)

    df_inst_sexo = pd.read_excel("nivel_instruccion.xlsx", sheet_name="Por_Sexo").rename(columns=inst_cols_map)
    df_inst_sexo["censo"] = 2011
    for col in df_inst_sexo.columns:
        if col not in ["censo", "sexo"]:
            df_inst_sexo[col] = pd.to_numeric(df_inst_sexo[col], errors="coerce").fillna(0).astype(int)
    df_inst_sexo.to_sql("instruccion_sexo", conn, if_exists="replace", index=False)

    print("--- 6. Situación Conyugal (Estado Lara) ---")
    conyugal_cols = {
        "Grupo de edad": "grupo_edad",
        "Unido(a)": "unido",
        "Casado(a)": "casado",
        "Soltero(a)": "soltero",
        "Separado(a) de unión o matrimonio": "separado",
        "Divorciado(a)": "divorciado",
        "Viudo(a) de unión o matrimonio": "viudo",
        "Total": "total"
    }

    all_conyugal_rows = []
    for sheet_name, sex_name, tbl_name in [("Hombres", "Hombre", "conyugal_hombres"), ("Mujeres", "Mujer", "conyugal_mujeres"), ("Total", "Total", "conyugal_total")]:
        df_c = pd.read_excel("situacion_conyugal.xlsx", sheet_name=sheet_name).rename(columns=conyugal_cols)
        df_c["censo"] = 2011
        for col in df_c.columns:
            if col not in ["censo", "grupo_edad"]:
                df_c[col] = pd.to_numeric(df_c[col], errors="coerce").fillna(0).astype(int)
        df_c.to_sql(tbl_name, conn, if_exists="replace", index=False)

        df_c_long = df_c.copy()
        df_c_long["sexo"] = sex_name
        all_conyugal_rows.append(df_c_long)

    df_conyugal_all = pd.concat(all_conyugal_rows, ignore_index=True)
    cols_conyugal = ["censo", "sexo", "grupo_edad", "unido", "casado", "soltero", "separado", "divorciado", "viudo", "total"]
    df_conyugal_all[cols_conyugal].to_sql("conyugal_sexo_edad", conn, if_exists="replace", index=False)

    print("--- 7. Fuerza de Trabajo y Actividad Económica (TRABAJO.xlsx) ---")
    df_raw_ft = pd.read_excel("TRABAJO.xlsx", header=None)
    c2011 = next((c for c in range(df_raw_ft.shape[1]) if "2011" in str(df_raw_ft.iloc[1, c])), 17)

    # Cuadro 04
    grupos_ft = ["15 - 24", "25 - 44", "45 - 64", "65 Y MAS"]
    rows_activa = {df_raw_ft.iloc[r, 3].strip(): int(df_raw_ft.iloc[r, c2011]) for r in [98, 100, 102, 104]}
    rows_ocupada = {df_raw_ft.iloc[r, 4].strip(): int(df_raw_ft.iloc[r, c2011]) for r in [108, 110, 112, 114]}
    rows_desocupada = {df_raw_ft.iloc[r, 4].strip(): int(df_raw_ft.iloc[r, c2011]) for r in [118, 120, 122, 124]}
    rows_inactiva = {df_raw_ft.iloc[r, 3].strip(): int(df_raw_ft.iloc[r, c2011]) for r in [128, 130, 132, 134]}

    df_ft_2011 = pd.DataFrame({
        "grupo_edad": grupos_ft,
        "poblacion_activa": [rows_activa[g] for g in grupos_ft],
        "ocupados": [rows_ocupada[g] for g in grupos_ft],
        "desocupados": [rows_desocupada[g] for g in grupos_ft],
        "inactivos": [rows_inactiva[g] for g in grupos_ft]
    })
    df_ft_2011["total_pet_15mas"] = df_ft_2011["poblacion_activa"] + df_ft_2011["inactivos"]
    tot_ft = {
        "grupo_edad": "Total (15 y más)",
        "poblacion_activa": df_ft_2011["poblacion_activa"].sum(),
        "ocupados": df_ft_2011["ocupados"].sum(),
        "desocupados": df_ft_2011["desocupados"].sum(),
        "inactivos": df_ft_2011["inactivos"].sum(),
        "total_pet_15mas": df_ft_2011["total_pet_15mas"].sum()
    }
    df_ft_2011 = pd.concat([df_ft_2011, pd.DataFrame([tot_ft])], ignore_index=True)
    df_ft_2011["censo"] = 2011
    df_ft_2011[["censo", "grupo_edad", "poblacion_activa", "ocupados", "desocupados", "inactivos", "total_pet_15mas"]].to_sql("fuerza_trabajo_edad", conn, if_exists="replace", index=False)

    # Cuadro 05
    branch_rows = [
        (162, "Agricultura, Pecuaria y Caza"),
        (169, "Industria Manufacturera"),
        (176, "Construcción"),
        (183, "Comercio, Restaurantes y Hoteles"),
        (190, "Transporte, Almacenamiento y Comunicaciones"),
        (197, "Establecimientos Financieros y Seguros"),
        (204, "Servicios Comunales, Sociales y Personales"),
        (211, "Explotación de Minas y Canteras"),
        (218, "Electricidad, Gas y Agua"),
        (225, "No Declaradas / No Especificadas")
    ]
    data_ramas = []
    for start_r, name in branch_rows:
        activa = int(df_raw_ft.iloc[start_r + 1, c2011])
        ocupada = int(df_raw_ft.iloc[start_r + 3, c2011])
        desocupada = int(df_raw_ft.iloc[start_r + 5, c2011])
        data_ramas.append({
            "rama_actividad": name,
            "poblacion_activa": activa,
            "ocupados": ocupada,
            "desocupados": desocupada
        })
    df_act_econ = pd.DataFrame(data_ramas)
    tot_pea = {
        "rama_actividad": "Total PEA",
        "poblacion_activa": df_act_econ["poblacion_activa"].sum(),
        "ocupados": df_act_econ["ocupados"].sum(),
        "desocupados": df_act_econ["desocupados"].sum()
    }
    df_act_econ = pd.concat([df_act_econ, pd.DataFrame([tot_pea])], ignore_index=True)
    df_act_econ["censo"] = 2011
    df_act_econ[["censo", "rama_actividad", "poblacion_activa", "ocupados", "desocupados"]].to_sql("actividad_economica_ramas", conn, if_exists="replace", index=False)

    # Serie histórica 1999-2025 (Cuadro 01)
    years_ft = [int(y) for y in df_raw_ft.iloc[1, 5:] if pd.notna(y)]
    indicators_ft = {
        "poblacion_total": 2,
        "pet_15mas": 3,
        "poblacion_activa": 5,
        "tasa_actividad_pct": 6,
        "poblacion_ocupada": 7,
        "tasa_ocupacion_pct": 8,
        "poblacion_desocupada": 9,
        "tasa_desocupacion_pct": 10,
        "poblacion_inactiva": 15,
        "tasa_inactividad_pct": 16,
        "estudiantes": 17,
        "quehaceres_hogar": 19,
        "incapacitados": 21
    }
    ft_hist_rows = []
    for idx_y, y in enumerate(years_ft):
        col_idx = 5 + idx_y
        r_dict = {"anio": y}
        for ind_name, r_num in indicators_ft.items():
            val = df_raw_ft.iloc[r_num, col_idx]
            try:
                r_dict[ind_name] = round(float(val), 2)
            except:
                r_dict[ind_name] = None
        ft_hist_rows.append(r_dict)
    pd.DataFrame(ft_hist_rows).to_sql("fuerza_trabajo_serie", conn, if_exists="replace", index=False)

    print("--- 8. Estadísticas Vitales (Matrimonios y Nacimientos) ---")
    # Matrimonios Entidad (1996-2017)
    df_mat_raw = pd.read_excel("POR-ENTIDAD-Matrimonios.xls", header=None)
    years_mat = [int(y) for y in df_mat_raw.iloc[2, 1:] if pd.notna(y)]
    df_mat_clean = df_mat_raw.iloc[3:, :len(years_mat)+1].dropna(subset=[0]).copy()
    df_mat_clean.columns = ["entidad"] + years_mat
    df_mat_clean["entidad"] = df_mat_clean["entidad"].astype(str).str.strip()
    df_mat_clean = df_mat_clean[
        (~df_mat_clean["entidad"].str.startswith("Estado:")) &
        (~df_mat_clean["entidad"].str.contains("Nota|Fuente", case=False, na=False))
    ].reset_index(drop=True)
    df_mat_long = df_mat_clean.melt(id_vars=["entidad"], var_name="anio", value_name="matrimonios")
    df_mat_long["anio"] = df_mat_long["anio"].astype(int)
    df_mat_long["matrimonios"] = pd.to_numeric(df_mat_long["matrimonios"], errors="coerce").fillna(0).astype(int)
    df_mat_long.to_sql("matrimonios_entidad", conn, if_exists="replace", index=False)

    # Matrimonios y Nacimientos Municipales (2013-2017)
    def parse_mun_vital(filepath, metric_name):
        df_raw = pd.read_excel(filepath, header=None)
        years = [int(y) for y in df_raw.iloc[2, 2:] if pd.notna(y)]
        rows = []
        current_entidad = None
        for r in range(3, len(df_raw)):
            row = df_raw.iloc[r]
            label = str(row[1]).strip() if pd.notna(row[1]) else ""
            if not label or label == "nan":
                continue
            if "Estado" in label or label == "Distrito Capital":
                current_entidad = label.replace("Estado", "").strip()
            vals = row[2:2+len(years)].values
            if any(pd.notna(v) for v in vals):
                for y_idx, y in enumerate(years):
                    val = vals[y_idx]
                    try:
                        val_num = int(float(val)) if pd.notna(val) else 0
                    except:
                        val_num = 0
                    rows.append({
                        "entidad": current_entidad if current_entidad else "Nacional",
                        "municipio": label,
                        "anio": y,
                        metric_name: val_num
                    })
        return pd.DataFrame(rows)

    df_mat_mun = parse_mun_vital("POR-MUNICIPIOS-Matrimonios.xls", "matrimonios")
    df_mat_mun.to_sql("matrimonios_municipio", conn, if_exists="replace", index=False)

    df_nac_mun = parse_mun_vital("POR-MUNICIPIOS-nacimientos.xls", "nacimientos")
    df_nac_mun.to_sql("nacimientos_municipio", conn, if_exists="replace", index=False)

    print("--- 9. Coeficiente de Gini Histórico ---")
    df_gini_raw = pd.read_excel("COEFICIENTE-GINI.xlsx", header=None).dropna(how="all", axis=0).dropna(how="all", axis=1)
    df_gini_clean = df_gini_raw.iloc[2:].copy()
    df_gini_clean.columns = ["anio", "coeficiente_gini"]
    df_gini_clean["anio"] = df_gini_clean["anio"].astype(int)
    df_gini_clean["coeficiente_gini"] = df_gini_clean["coeficiente_gini"].astype(float)
    df_gini_clean.to_sql("gini_historico", conn, if_exists="replace", index=False)

    print("--- 10. Servicios Básicos (Censo 2011) ---")
    df_serv = pd.read_excel("Servicios-Censo_2011.xlsx", sheet_name="Servicios Básicos", header=2)
    df_serv = df_serv.dropna(how="all", axis=1).dropna(how="all", axis=0)
    df_serv.columns = [str(c).strip() for c in df_serv.columns]
    df_serv = df_serv.loc[:, ~df_serv.columns.str.startswith("Unnamed")]
    df_serv = df_serv.dropna(subset=["Código UBIGEO"]).reset_index(drop=True)
    df_serv = df_serv[df_serv["Código UBIGEO"].astype(str).str.strip().str.match(r"^\d+$")].reset_index(drop=True)
    df_serv = df_serv.rename(columns={
        "Código UBIGEO": "codigo_ubigeo",
        "Entidad federal": "entidad",
        "Municipio": "municipio",
        "Parroquia": "parroquia",
        "Total": "total_hogares",
        "Con Deficit en Servicios Básicos": "con_deficit",
        "Con Servicios Básicos": "con_servicios"
    })
    df_serv["censo"] = 2011
    df_serv["codigo_ubigeo"] = df_serv["codigo_ubigeo"].astype(str).str.zfill(6)
    for col in ["total_hogares", "con_deficit", "con_servicios"]:
        df_serv[col] = pd.to_numeric(df_serv[col], errors="coerce").fillna(0).astype(int)
    cols_serv = ["censo", "codigo_ubigeo", "entidad", "municipio", "parroquia", "total_hogares", "con_servicios", "con_deficit"]
    df_serv[cols_serv].to_sql("servicios_parroquia", conn, if_exists="replace", index=False)

    # Migración interna inter-estadal 
    df_mig_raw = pd.read_excel("Servicios-Censo_2011.xlsx", sheet_name="Sheet3", header=None)
    df_mig = df_mig_raw.iloc[16:, 1:9].copy()
    df_mig.columns = ["codigo_ubigeo", "entidad", "municipio", "parroquia", "en_la_entidad", "en_otra_entidad", "en_el_exterior", "total"]
    df_mig = df_mig[df_mig["codigo_ubigeo"].astype(str).str.strip().str.match(r"^\d+$")].reset_index(drop=True)
    df_mig["censo"] = 2011
    df_mig["codigo_ubigeo"] = df_mig["codigo_ubigeo"].astype(str).str.zfill(6)
    for c in ["en_la_entidad", "en_otra_entidad", "en_el_exterior", "total"]:
        df_mig[c] = pd.to_numeric(df_mig[c], errors="coerce").fillna(0).astype(int)
    df_mig[["censo", "codigo_ubigeo", "entidad", "municipio", "parroquia", "en_la_entidad", "en_otra_entidad", "en_el_exterior", "total"]].to_sql("migracion_interna_parroquia", conn, if_exists="replace", index=False)

    print("--- 11. Viviendas, Hogares y Personas (Censo 2011) ---")
    df_personas_p = pd.read_excel("VIVIENDAS-HOGARES-Y-PERSONAS-CENSO-2011.xlsx", sheet_name="PERSONAS PARROQUIA", header=1)
    df_personas_p = df_personas_p.dropna(subset=["UBIGEO", "PARROQUIA"]).reset_index(drop=True)
    df_personas_p = df_personas_p[df_personas_p["UBIGEO"] != "TOTAL"].copy()
    df_personas_p = df_personas_p.rename(columns={
        "UBIGEO": "codigo_ubigeo",
        "PARROQUIA": "parroquia",
        "NACIONAL": "total_personas",
        "MENOR DE 15 AÑOS": "menor_15",
        "DE 15 A 64 AÑOS": "de_15_a_64",
        "DE 65 AÑOS Y MÁS": "de_65_mas",
        "RAZÓN DE DEPENDENCIA": "razon_dependencia",
        "PROMEDIO DE EDAD": "promedio_edad",
        "ÍNDICE DE MASCULINIDAD": "indice_masculinidad",
        " POBLACIÓN URBANA": "pob_urbana",
        "POBLACIÓN RURAL": "pob_rural",
        "   POBLACIÓN DE 10 AÑOS Y MÁS ANALFABETA": "analfabetas_10mas"
    })
    df_personas_p["censo"] = 2011
    df_personas_p["codigo_ubigeo"] = df_personas_p["codigo_ubigeo"].astype(str).str.zfill(6)
    p_cols_to_keep = ["censo", "codigo_ubigeo", "parroquia", "total_personas", "menor_15", "de_15_a_64", "de_65_mas", "razon_dependencia", "promedio_edad", "indice_masculinidad", "pob_urbana", "pob_rural", "analfabetas_10mas"]
    for col in p_cols_to_keep:
        if col in df_personas_p.columns and col not in ["censo", "codigo_ubigeo", "parroquia"]:
            df_personas_p[col] = pd.to_numeric(df_personas_p[col], errors="coerce").fillna(0)
    df_personas_p[[c for c in p_cols_to_keep if c in df_personas_p.columns]].to_sql("personas_parroquia", conn, if_exists="replace", index=False)

    df_viv_p = pd.read_excel("VIVIENDAS-HOGARES-Y-PERSONAS-CENSO-2011.xlsx", sheet_name="VIVIENDA PARROQUIA", header=1)
    df_viv_p = df_viv_p.dropna(subset=["UBIGEO", "PARROQUIA"]).reset_index(drop=True)
    df_viv_p = df_viv_p[df_viv_p["UBIGEO"] != "TOTAL"].copy()
    df_viv_p = df_viv_p.rename(columns={
        "UBIGEO": "codigo_ubigeo",
        "PARROQUIA": "parroquia",
        "VIVIENDAS FAMILIARES Y COLECTIVAS": "total_viviendas",
        "VIVIENDAS FAMILIARES OCUPADAS": "viviendas_ocupadas",
        "DESOCUPADAS": "viviendas_desocupadas"
    })
    df_viv_p["censo"] = 2011
    df_viv_p["codigo_ubigeo"] = df_viv_p["codigo_ubigeo"].astype(str).str.zfill(6)
    v_cols = ["censo", "codigo_ubigeo", "parroquia", "total_viviendas", "viviendas_ocupadas", "viviendas_desocupadas"]
    for col in v_cols:
        if col in df_viv_p.columns and col not in ["censo", "codigo_ubigeo", "parroquia"]:
            df_viv_p[col] = pd.to_numeric(df_viv_p[col], errors="coerce").fillna(0).astype(int)
    df_viv_p[[c for c in v_cols if c in df_viv_p.columns]].to_sql("vivienda_parroquia", conn, if_exists="replace", index=False)

    # Ingesta coNDAS-HOGARES-Y-PERSONAS-CENSO-2011
    viviendas_extra_sheets = [
        ("HOGARES PARROQUIA", "hogares_parroquia"),
        ("HOGARES MUNICIPIO", "hogares_municipio"),
        ("HOGARES ENTIDAD", "hogares_entidad"),
        ("VIVIENDA MUNICIPIO", "vivienda_municipio"),
        ("VIVIENDA ENTIDAD", "vivienda_entidad"),
        ("PERSONAS MUNICIPIO", "personas_municipio"),
        ("PERSONAS ENTIDAD", "personas_entidad"),
    ]
    f_viv = "VIVIENDAS-HOGARES-Y-PERSONAS-CENSO-2011.xlsx"
    for s_name, tbl_name in viviendas_extra_sheets:
        df_sheet = pd.read_excel(f_viv, sheet_name=s_name, header=1)
        df_sheet = df_sheet.loc[:, ~df_sheet.columns.str.startswith("Unnamed")]
        col_u = [c for c in df_sheet.columns if "UBIGEO" in str(c).upper()]
        if col_u:
            df_sheet = df_sheet.dropna(subset=[col_u[0]]).copy()
            df_sheet = df_sheet[df_sheet[col_u[0]].astype(str).str.strip().str.match(r"^\d+$")].reset_index(drop=True)
            pad_len = 6 if "PARROQUIA" in s_name else (4 if "MUNICIPIO" in s_name else 2)
            df_sheet[col_u[0]] = df_sheet[col_u[0]].astype(str).str.zfill(pad_len)
        df_sheet.columns = [clean_col(c) for c in df_sheet.columns]
        df_sheet["censo"] = 2011
        txt_cols = ["censo", "ubigeo", "parroquia", "entidad_federal", "entidad_y_municipio"]
        for c in df_sheet.columns:
            if c not in txt_cols and not isinstance(df_sheet[c], pd.DataFrame):
                df_sheet[c] = pd.to_numeric(df_sheet[c], errors="coerce").fillna(0)
        df_sheet.to_sql(tbl_name, conn, if_exists="replace", index=False)

    print("--- 12. Centros Poblados de Lara (Lara.xls) ---")
    df_lara_cp = pd.read_excel("Lara.xls")
    df_lara_cp.columns = [clean_col(c) for c in df_lara_cp.columns]
    df_lara_cp["censo"] = 2011
    df_lara_cp.to_sql("lara_centros_poblados", conn, if_exists="replace", index=False)

    # Índices para alta velocidad de consulta y preparación para UNION con Censo 2001
    print("--- Creando índices optimizados ---")
    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_pob_sexo_ubigeo ON pob_sexo_parroquia (censo, codigo_ubigeo);",
        "CREATE INDEX IF NOT EXISTS idx_pob_sexo_entidad ON pob_sexo_parroquia (entidad);",
        "CREATE INDEX IF NOT EXISTS idx_pob_edad_ubigeo ON pob_edad_parroquia (censo, codigo_ubigeo);",
        "CREATE INDEX IF NOT EXISTS idx_pob_nac_ubigeo ON pob_nacimiento_parroquia (censo, codigo_ubigeo);",
        "CREATE INDEX IF NOT EXISTS idx_alf_edad ON alfabetismo_edad (censo, grupo_edad);",
        "CREATE INDEX IF NOT EXISTS idx_inst_edad ON instruccion_edad (censo, grupo_edad);",
        "CREATE INDEX IF NOT EXISTS idx_cony_total ON conyugal_total (censo, grupo_edad);",
        "CREATE INDEX IF NOT EXISTS idx_mat_ent ON matrimonios_entidad (entidad, anio);",
        "CREATE INDEX IF NOT EXISTS idx_mat_mun ON matrimonios_municipio (entidad, municipio, anio);",
        "CREATE INDEX IF NOT EXISTS idx_nac_mun ON nacimientos_municipio (entidad, municipio, anio);",
        "CREATE INDEX IF NOT EXISTS idx_ft_serie ON fuerza_trabajo_serie (anio);",
        "CREATE INDEX IF NOT EXISTS idx_serv_ubigeo ON servicios_parroquia (censo, codigo_ubigeo);"
    ]
    for idx_sql in indexes:
        cur.execute(idx_sql)

    conn.commit()
    conn.close()
    print(f"\n¡Base de datos {DB_PATH} construida con éxito!")

if __name__ == "__main__":
    build_database()
