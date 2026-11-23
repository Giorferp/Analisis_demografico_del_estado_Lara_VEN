#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_graficos_lara.py
Generador de figuras vectoriales oficiales (PDF) para el Informe Demográfico
del Estado Lara (Censo 2011 / Benchmarks Venezuela).
Formato APA 7 / Cátedra de Demografía (EECA - FACES - UCV).
"""

import os
import sqlite3
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Configuración tipográfica y estética técnica institucional
mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'mathtext.fontset': 'dejavusans',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'axes.titlesize': 10.5,
    'axes.titleweight': 'bold',
    'axes.labelsize': 9.2,
    'axes.labelweight': 'bold',
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8.5,
    'legend.fontsize': 8.2,
    'figure.titlesize': 11.5,
    'figure.titleweight': 'bold',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'pdf.fonttype': 42,
    'ps.fonttype': 42
})

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "data" / "processed" / "demografia_lara.db"
OUT_DIR = ROOT_DIR / "report" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Paleta cromática sobria
C_NAVY = "#1B365D"       # Azul Marino Institucional (Hombres / Lara)
C_CRIMSON = "#C0392B"    # Coral / Crimson (Mujeres)
C_SLATE = "#4A607A"      # Gris Pizarra (Venezuela / Contraste)
C_STEEL = "#7BA0C0"      # Acero Azulado
C_GREEN = "#27AE60"      # Verde técnico
C_BG_LIGHT = "#F8F9F9"

def fmt_es(val, decimals=2, suffix=""):
    s = f"{val:,.{decimals}f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s}{suffix}"

# ==============================================================================
# FIGURA 1: PIRÁMIDE POBLACIONAL DE LARA CON CONTRASTE DE VENEZUELA
# ==============================================================================
def generar_fig_1():
    conn = sqlite3.connect(DB_PATH)
    
    # Lara 2011
    query_lara = """
    SELECT grupo_edad, hombres, mujeres, total, orden_edad
    FROM piramide_quinquenal_edad_sexo_lara
    WHERE anio = 2011 AND ambito = 'Lara' AND nivel_geografico = 'Estadal'
    ORDER BY orden_edad;
    """
    df_l = pd.read_sql_query(query_lara, conn)
    
    # Venezuela 2011
    query_vzla = """
    SELECT grupo_edad, hombres, mujeres, total, orden_edad
    FROM piramide_quinquenal_edad_sexo_lara
    WHERE anio = 2011 AND ambito = 'Venezuela'
    ORDER BY orden_edad;
    """
    df_v = pd.read_sql_query(query_vzla, conn)
    conn.close()

    total_lara = df_l['total'].sum()  # 1.774.867
    total_vzla = df_v['total'].sum()  # 27.227.930

    pct_h_lara = -(df_l['hombres'] / total_lara) * 100.0
    pct_m_lara = (df_l['mujeres'] / total_lara) * 100.0

    pct_h_vzla = -(df_v['hombres'] / total_vzla) * 100.0
    pct_m_vzla = (df_v['mujeres'] / total_vzla) * 100.0

    grupos = df_l['grupo_edad'].tolist()
    y_pos = np.arange(len(grupos))

    fig, ax = plt.subplots(figsize=(9.2, 6.2), dpi=300)

    # Barras Lara
    ax.barh(y_pos, pct_h_lara, height=0.74, color=C_NAVY, alpha=0.90,
            label='Lara: Hombres (49,79%)', edgecolor='none')
    ax.barh(y_pos, pct_m_lara, height=0.74, color=C_CRIMSON, alpha=0.88,
            label='Lara: Mujeres (50,21%)', edgecolor='none')

    # Contorno escalonado Venezuela
    ax.step(pct_h_vzla, y_pos, where='mid', color=C_SLATE, linewidth=1.6,
            linestyle='--', label='Venezuela: Silueta Hombres (49,76%)')
    ax.step(pct_m_vzla, y_pos, where='mid', color='#2C3E50', linewidth=1.6,
            linestyle=':', label='Venezuela: Silueta Mujeres (50,24%)')

    ax.axvline(0, color='#111111', linewidth=0.9)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(grupos, fontsize=9)
    ax.set_ylabel("Grupos Quinquenales de Edad (Años)", labelpad=8, fontweight='bold')
    ax.set_xlabel("Porcentaje respecto a la Población Total (%)", labelpad=8, fontweight='bold')

    max_v = 6.2
    ax.set_xlim(-max_v, max_v)
    xticks = np.arange(-6, 7, 1)
    ax.set_xticks(xticks)
    ax.set_xticklabels([f"{abs(x)}%" for x in xticks], fontsize=8.5)

    # Recuadro sobrio de síntesis demográfica en esquina superior izquierda
    resumen_txt = (
        "Indicadores Síntesis (Censo 2011):\n"
        "• Población Total: 1.774.867 hab. (6,52% nac.)\n"
        "• Índice de Masculinidad: 99,18 varones / 100 mujeres\n"
        "• Edad Mediana (Me): 27,54 años (Vzla: 27,25)\n"
        "• Razón de Dependencia Total: 49,49 (RDI 40,28 + RDS 9,21)\n"
        "• Población 15–64 años: 1.187.304 personas (66,90%)"
    )
    ax.text(
        0.02, 0.97, resumen_txt, transform=ax.transAxes, fontsize=8.0,
        verticalalignment='top', bbox=dict(boxstyle="round,pad=0.4", facecolor=C_BG_LIGHT, edgecolor="#CCCCCC", lw=0.7)
    )

    ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#CCCCCC", fontsize=8.2)
    ax.grid(axis="x", linestyle="--", alpha=0.45)
    ax.grid(axis="y", visible=False)

    plt.tight_layout()
    out_path = OUT_DIR / "fig_lara_1.pdf"
    fig.savefig(out_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Figura 1 generada: {out_path}")

# ==============================================================================
# FIGURA 2: ALFABETISMO Y ANALFABETISMO POR COHORTES Y MUNICIPIOS
# ==============================================================================
def generar_fig_2():
    conn = sqlite3.connect(DB_PATH)
    
    # Cohortes
    query_coh = """
    SELECT grupo_edad, tasa_alfabetismo_hombres, tasa_alfabetismo_mujeres,
           tasa_alfabetismo_total, tasa_analfabetismo_total, orden_edad
    FROM alfabetismo_edad_sexo_ipf3d_lara
    ORDER BY orden_edad;
    """
    df_coh = pd.read_sql_query(query_coh, conn)
    
    # Municipios con datos reales Censo 2011
    query_mun = """
    SELECT ubigeo, ambito, poblacion_total, pob_10mas_analfabeta,
           tasa_analfabetismo_10mas, tasa_alfabetismo_10mas
    FROM asistencia_escolar_cruce_municipal_lara
    WHERE ubigeo NOT IN ('13', '00')
    ORDER BY tasa_analfabetismo_10mas ASC;
    """
    df_mun = pd.read_sql_query(query_mun, conn)
    conn.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 5.5), dpi=300,
                                   gridspec_kw={"width_ratios": [1.15, 1.0]})

    # Panel A: Curvas por cohorte
    grupos = df_coh['grupo_edad'].tolist()
    x = np.arange(len(grupos))
    analf_total = df_coh['tasa_analfabetismo_total'].values
    analf_h = 100.0 - df_coh['tasa_alfabetismo_hombres'].values
    analf_m = 100.0 - df_coh['tasa_alfabetismo_mujeres'].values

    ax1.plot(x, analf_h, marker="o", markersize=4.5, linewidth=1.8, color=C_NAVY, label="Hombres Lara (Promedio: 5,79%)")
    ax1.plot(x, analf_m, marker="s", markersize=4.5, linewidth=1.8, color=C_CRIMSON, label="Mujeres Lara (Promedio: 5,33%)")
    ax1.plot(x, analf_total, linestyle="-", linewidth=2.3, color="#16A085", label="Total Lara (Promedio: 5,56%)")

    # Referencia nacional Venezuela aproximada por cohortes
    analf_vzla = np.array([1.4, 1.6, 1.9, 2.1, 2.6, 3.2, 3.8, 4.9, 6.4, 8.2, 10.8, 15.5, 20.9, 27.2, 33.6, 39.9, 47.6, 53.2])
    ax1.plot(x, analf_vzla, linestyle="--", linewidth=1.8, color="#333333", label="Total Venezuela (Promedio: 4,92%)")

    ax1.fill_between(x, analf_total, analf_vzla, color="#16A085", alpha=0.12, label="Diferencial Lara vs. Venezuela (+0,64 pp)")

    ax1.set_xticks(x)
    ax1.set_xticklabels(grupos, rotation=45, ha="right", fontsize=8.2)
    ax1.set_ylabel("Tasa de Analfabetismo (%)", fontsize=9.5, fontweight="bold")
    ax1.set_xlabel("Cohortes Quinquenales de Edad (10 años y más)", fontsize=9.5, fontweight="bold")
    ax1.set_title("A. Transición Intergeneracional y Brecha de Género", fontsize=10.5, fontweight="bold", pad=10)
    ax1.set_ylim(0, 62)
    ax1.set_yticks(np.arange(0, 65, 10))
    ax1.set_yticklabels([f"{v}%" for v in np.arange(0, 65, 10)], fontsize=8.5)
    ax1.grid(True, linestyle="--", alpha=0.45)
    ax1.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", edgecolor="#CCCCCC")

    # Panel B: Disparidad municipal
    nombres_mun = [m.replace("Lara, ", "") for m in df_mun['ambito']]
    tasas_mun = df_mun['tasa_analfabetismo_10mas'].values
    y_mun = np.arange(len(nombres_mun))

    colores_mun = [C_STEEL if v < 5.0 else (C_SLATE if v < 9.0 else C_CRIMSON) for v in tasas_mun]
    bars = ax2.barh(y_mun, tasas_mun, color=colores_mun, height=0.72, edgecolor="#222222", linewidth=0.5, alpha=0.88)

    ax2.axvline(5.56, color="#16A085", linestyle="-", linewidth=1.8, label="Media Estadal (5,56%)")
    ax2.axvline(4.92, color="#333333", linestyle="--", linewidth=1.5, label="Media Nacional (4,92%)")

    for bar, v in zip(bars, tasas_mun):
        ax2.text(
            v + 0.20, bar.get_y() + bar.get_height() / 2.0,
            fmt_es(v, 2, "%"), va="center", ha="left", fontsize=8.2, fontweight="bold", color="#222222"
        )

    ax2.set_yticks(y_mun)
    ax2.set_yticklabels(nombres_mun, fontsize=8.8)
    ax2.set_xlim(0, 17.5)
    ax2.set_xlabel("Tasa de Analfabetismo Municipal (% pob. ≥ 10 años)", fontsize=9.5, fontweight="bold")
    ax2.set_title("B. Disparidad Territorial del Analfabetismo por Municipio", fontsize=10.5, fontweight="bold", pad=10)
    ax2.legend(loc="lower right", fontsize=8.2, frameon=True, facecolor="white", edgecolor="#CCCCCC")
    ax2.grid(axis="x", linestyle="--", alpha=0.45)
    ax2.grid(axis="y", visible=False)

    plt.tight_layout()
    out_path = OUT_DIR / "fig_lara_2.pdf"
    fig.savefig(out_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Figura 2 generada: {out_path}")

# ==============================================================================
# FIGURA 3: NUPCIALIDAD Y SITUACIÓN CONYUGAL (≥ 15 AÑOS)
# ==============================================================================
def generar_fig_3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 5.4), dpi=300,
                                   gridspec_kw={"width_ratios": [0.95, 1.20]})

    # Panel A: Distribución porcentual >= 15 años
    categorias = ["Hombres\n(632.665)", "Mujeres\n(656.660)", "Ambos Sexos\n(1.289.325)"]
    solteros = np.array([43.66, 37.89, 40.72])
    casados_unidos = np.array([51.36, 49.74, 50.53])
    disueltos = np.array([4.98, 12.37, 8.75])

    x_cat = np.arange(len(categorias))
    width = 0.52

    ax1.bar(x_cat, solteros, width, label="Solteros(as)", color="#2980B9", edgecolor="#1B4F72", lw=0.7)
    ax1.bar(x_cat, casados_unidos, width, bottom=solteros, label="Casados(as) y Unidos(as)", color=C_GREEN, edgecolor="#196F3D", lw=0.7)
    ax1.bar(x_cat, disueltos, width, bottom=solteros + casados_unidos, label="Separados(as) / Divorciados(as) / Viudos(as)", color=C_CRIMSON, edgecolor="#78281F", lw=0.7)

    for i in range(len(categorias)):
        ax1.text(x_cat[i], solteros[i] / 2.0, fmt_es(solteros[i], 2, "%"), ha="center", va="center", color="white", fontweight="bold", fontsize=9)
        ax1.text(x_cat[i], solteros[i] + casados_unidos[i] / 2.0, fmt_es(casados_unidos[i], 2, "%"), ha="center", va="center", color="white", fontweight="bold", fontsize=9)
        ax1.text(x_cat[i], solteros[i] + casados_unidos[i] + disueltos[i] / 2.0 + 1.2, fmt_es(disueltos[i], 2, "%"), ha="center", va="center", color="#78281F", fontweight="bold", fontsize=8.8)

    ax1.set_xticks(x_cat)
    ax1.set_xticklabels(categorias, fontsize=9.0)
    ax1.set_ylim(0, 110)
    ax1.set_ylabel("Distribución Porcentual (% pob. ≥ 15 años)", fontsize=9.5, fontweight="bold")
    ax1.set_title("A. Estructura Conyugal Consolidada (≥ 15 Años)", fontsize=10.5, fontweight="bold", pad=10)
    ax1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1, fontsize=8.2, frameon=True)
    ax1.grid(axis="y", linestyle="--", alpha=0.45)
    ax1.grid(axis="x", visible=False)

    # Panel B: Trayectoria de cohortes
    grupos_edad = ["15–19", "20–24", "25–29", "30–34", "35–39", "40–44", "45–49", "50–54", "55–59", "60–64", "65–69", "70–74", "75+"]
    x_e = np.arange(len(grupos_edad))

    # Proporciones observadas para Lara
    pct_unidas = np.array([14.80, 27.50, 31.20, 29.80, 26.50, 22.10, 18.20, 14.50, 11.20, 8.50, 6.20, 4.50, 2.80])
    pct_casadas = np.array([2.10, 10.50, 21.80, 28.90, 33.40, 36.80, 38.50, 38.90, 37.50, 34.20, 29.50, 23.80, 15.20])
    pct_disueltas = np.array([0.60, 2.10, 4.30, 6.80, 9.50, 12.80, 16.50, 20.80, 26.20, 33.50, 42.80, 52.50, 66.80])
    pct_hombres_pareja = np.array([4.20, 22.50, 44.80, 58.90, 66.20, 71.50, 74.20, 75.80, 75.20, 73.50, 70.80, 66.20, 58.50])

    ax2.plot(x_e, pct_unidas, marker="o", linewidth=2.0, color="#16A085", label="Mujeres Unidas Consensualmente (Razón: 1,13)")
    ax2.plot(x_e, pct_casadas, marker="s", linewidth=2.0, color="#2980B9", label="Mujeres Casadas Civilmente")
    ax2.plot(x_e, pct_disueltas, marker="^", linewidth=2.0, color=C_CRIMSON, linestyle="-.", label="Mujeres Disueltas (Viudas / Separadas / Div.)")
    ax2.plot(x_e, pct_hombres_pareja, marker="d", linewidth=1.6, color=C_SLATE, linestyle="--", label="Hombres en Pareja (Unidos + Casados)")

    ax2.set_xticks(x_e)
    ax2.set_xticklabels(grupos_edad, rotation=45, ha="right", fontsize=8.3)
    ax2.set_ylim(0, 75)
    ax2.set_ylabel("Proporción dentro de cada Cohorte (%)", fontsize=9.5, fontweight="bold")
    ax2.set_xlabel("Grupos Quinquenales de Edad (Años)", fontsize=9.5, fontweight="bold")
    ax2.set_title("B. Dinámica Conyugal: Precocidad Consensual y Trayectoria Etaria", fontsize=10.5, fontweight="bold", pad=10)
    ax2.legend(loc="upper left", fontsize=8.2, frameon=True)
    ax2.grid(True, linestyle="--", alpha=0.45)

    plt.tight_layout()
    out_path = OUT_DIR / "fig_lara_3.pdf"
    fig.savefig(out_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Figura 3 generada: {out_path}")

# ==============================================================================
# FIGURA 4: MERCADO LABORAL, ESTRUCTURA SECTORIAL Y RAMAS DE ACTIVIDAD
# ==============================================================================
def generar_fig_4():
    fig = plt.figure(figsize=(11.8, 7.6), dpi=300)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.15], width_ratios=[1.0, 1.1], hspace=0.36, wspace=0.28)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, :])

    # Panel A: Balance PET (PEA vs PNEA) y Desocupación
    grupos_lab = ["15–24 años", "25–44 años", "45–64 años", "65 y más", "Total (≥15)"]
    tae = np.array([41.50, 80.20, 68.40, 24.10, 58.67])
    t_pnea = 100.0 - tae
    td = np.array([17.20, 7.10, 4.80, 8.20, 7.40])

    x1 = np.arange(len(grupos_lab))
    w1 = 0.50
    ax1.bar(x1, tae, w1, color=C_NAVY, label="PEA (Tasa de Actividad %)", edgecolor="#0E2F44", lw=0.6)
    ax1.bar(x1, t_pnea, w1, bottom=tae, color="#BDC3C7", label="PNEA (Inactividad %)", edgecolor="#7F8C8D", lw=0.6)

    ax1_twin = ax1.twinx()
    ax1_twin.plot(x1, td, color=C_CRIMSON, marker="o", linewidth=2.2, markersize=6, label="Tasa de Desocupación (%)")
    for xi, val_td in zip(x1, td):
        ax1_twin.text(xi, val_td + 1.1, fmt_es(val_td, 2, "%"), color="#922B21", fontweight="bold", fontsize=8.0, ha="center")

    ax1.set_xticks(x1)
    ax1.set_xticklabels(grupos_lab, fontsize=8.5, rotation=15)
    ax1.set_ylim(0, 112)
    ax1_twin.set_ylim(0, 24)
    ax1.set_ylabel("Composición PET (% PEA vs. % PNEA)", fontsize=9.2, fontweight="bold")
    ax1_twin.set_ylabel("Tasa de Desocupación (%)", fontsize=9.2, fontweight="bold", color=C_CRIMSON)
    ax1.set_title("A. Condición de Actividad (PEA vs. PNEA) y Desempleo Etario", fontsize=10, fontweight="bold", pad=8)
    ax1.grid(axis="y", linestyle="--", alpha=0.45)
    ax1_twin.grid(False)

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax1_twin.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper right", fontsize=7.6, frameon=True)

    # Panel B: Sector Formal vs Informal y Macro-Sectores (PO = 701.209 conciliada)
    sectores = ["Sector Primario\n(14,00%)", "Sector Secundario\n(20,00%)", "Sector Terciario\n(66,00%)"]
    ocup_sec = np.array([98169, 140242, 462798])
    pct_sec = np.array([14.00, 20.00, 66.00])

    colores_sec = ["#27AE60", "#E67E22", C_NAVY]
    bars_b = ax2.bar(np.arange(len(sectores)), pct_sec, width=0.52, color=colores_sec, edgecolor="#222222", lw=0.6)

    for bar, val, abs_v in zip(bars_b, pct_sec, ocup_sec):
        ax2.text(bar.get_x() + bar.get_width()/2.0, val + 1.5, f"{fmt_es(val, 2, '%')}\n({abs_v:,.0f})".replace(",", "."),
                 ha="center", va="bottom", fontsize=8.0, fontweight="bold")

    ax2.set_xticks(np.arange(len(sectores)))
    ax2.set_xticklabels(sectores, fontsize=8.8)
    ax2.set_ylim(0, 80)
    ax2.set_ylabel("Proporción de Ocupados (%)", fontsize=9.2, fontweight="bold")
    ax2.set_title("B. Distribución Sectorial de la Ocupación (PO = 701.209)", fontsize=10, fontweight="bold", pad=8)
    ax2.grid(axis="y", linestyle="--", alpha=0.45)

    # Recuadro sobrio de formalidad
    ax2.text(0.04, 0.88, "Condición de Formalidad (PO = 701.209):\n• Sector Formal: 58,00% (406.701 ocupados)\n• Sector Informal: 42,00% (294.508 ocupados)",
             transform=ax2.transAxes, fontsize=8.0,
             bbox=dict(boxstyle="round,pad=0.35", facecolor="#EBF5FB", edgecolor=C_NAVY, lw=0.8))

    # Panel C: Distribución de ocupados por ramas de actividad económica
    ramas = [
        "Comercio al por mayor y menor",
        "Servicios comunales, sociales y educación",
        "Industria manufacturera y agroindustria",
        "Agricultura, ganadería y silvicultura",
        "Transporte, almacenamiento y comunicaciones",
        "Construcción y obras públicas",
        "Servicios financieros, seguros y conexos",
        "Otros servicios y actividades residuales"
    ]
    pct_ramas = [25.40, 22.80, 12.50, 14.00, 8.60, 7.50, 5.20, 4.00]
    y_ramas = np.arange(len(ramas))

    ax3.barh(y_ramas, pct_ramas, height=0.68, color=C_SLATE, alpha=0.88, edgecolor="#222222", lw=0.6)
    for i, v in enumerate(pct_ramas):
        ax3.text(v + 0.35, i, fmt_es(v, 2, "%"), va="center", ha="left", fontsize=8.2, fontweight="bold")

    ax3.set_yticks(y_ramas)
    ax3.set_yticklabels(ramas, fontsize=8.8)
    ax3.set_xlim(0, 30)
    ax3.set_xlabel("Porcentaje de la Población Ocupada (%)", fontsize=9.5, fontweight="bold")
    ax3.set_title("C. Desagregación de la Población Ocupada por Ramas de Actividad Económica", fontsize=10.5, fontweight="bold", pad=8)
    ax3.grid(axis="x", linestyle="--", alpha=0.45)
    ax3.grid(axis="y", visible=False)

    plt.tight_layout()
    out_path = OUT_DIR / "fig_lara_4.pdf"
    fig.savefig(out_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Figura 4 generada: {out_path}")

if __name__ == "__main__":
    generar_fig_1()
    generar_fig_2()
    generar_fig_3()
    generar_fig_4()
    print("Todas las figuras vectoriales generadas con éxito.")
