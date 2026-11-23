#!/usr/bin/env python3
"""Compila el informe técnico LaTeX en PDF mediante XeLaTeX y limpia auxiliares."""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = ROOT_DIR / "report"
TEX_NAME = "Análisis_Demográfico_del_Estado_Lara.tex"
AUX_EXTENSIONS = (".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz")


def clean_aux_files(report_dir: Path) -> None:
    """Elimina archivos auxiliares generados durante la compilación LaTeX."""
    stem = Path(TEX_NAME).stem
    for ext in AUX_EXTENSIONS:
        aux = report_dir / f"{stem}{ext}"
        if aux.exists():
            aux.unlink()


def compile_report() -> int:
    """Ejecuta dos pasadas de XeLaTeX para resolver índice y referencias cruzadas."""
    xelatex = shutil.which("xelatex")
    if not xelatex:
        print("Error: 'xelatex' no se encuentra en PATH.", file=sys.stderr)
        return 1

    tex_path = REPORT_DIR / TEX_NAME
    if not tex_path.exists():
        print(f"Error: no existe {tex_path}", file=sys.stderr)
        return 1

    cmd = [xelatex, "-interaction=nonstopmode", "-halt-on-error", TEX_NAME]
    for step in (1, 2):
        print(f"Compilando {TEX_NAME} (pasada {step}/2)...")
        res = subprocess.run(cmd, cwd=REPORT_DIR, capture_output=True, text=True)
        if res.returncode != 0:
            print(res.stdout[-2000:])
            print(res.stderr, file=sys.stderr)
            return res.returncode

    clean_aux_files(REPORT_DIR)
    pdf_path = REPORT_DIR / f"{Path(TEX_NAME).stem}.pdf"
    size_kb = pdf_path.stat().st_size / 1024.0
    print(f"PDF compilado exitosamente: {pdf_path} ({size_kb:.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(compile_report())
