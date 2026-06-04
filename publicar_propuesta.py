#!/usr/bin/env python3
"""
Publica una propuesta HTML en systechub.com/propuestas/[slug]

Uso:
  python3 publicar_propuesta.py "Nombre Empresa" /ruta/a/propuesta.html
  python3 publicar_propuesta.py "Travex" /tmp/propuesta_travex.html

La URL resultante es: https://systechub.com/propuestas/[slug]
"""

import sys
import os
import re
import shutil
import subprocess
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────
WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_URL  = "https://systechub.com/propuestas"

# ── Helpers ──────────────────────────────────────────────────────────────────
def slugify(text: str) -> str:
    text = text.lower().strip()
    replacements = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","ñ":"n","ü":"u"}
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text.strip("-")

def run(cmd: list, cwd: str = WEB_ROOT) -> str:
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error en comando {' '.join(cmd)}:\n{result.stderr}")
    return result.stdout.strip()

# ── Main ─────────────────────────────────────────────────────────────────────
def publicar(empresa: str, html_path: str) -> str:
    slug        = slugify(empresa)
    dest_dir    = os.path.join(WEB_ROOT, "propuestas", slug)
    dest_file   = os.path.join(dest_dir, "index.html")
    url         = f"{BASE_URL}/{slug}"
    fecha       = datetime.now().strftime("%Y-%m-%d")

    # 1. Crear carpeta y copiar HTML
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(html_path, dest_file)
    print(f"✓ Propuesta copiada → propuestas/{slug}/index.html")

    # 2. Git add + commit + push
    run(["git", "add", f"propuestas/{slug}/"])
    run(["git", "commit", "-m", f"Propuesta: {empresa} ({fecha})"])
    print("✓ Commit creado")

    run(["git", "push"])
    print("✓ Push a GitHub — Netlify desplegando...")

    return url

# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    empresa   = sys.argv[1]
    html_path = sys.argv[2]

    if not os.path.isfile(html_path):
        print(f"Error: no se encontró el archivo {html_path}")
        sys.exit(1)

    url = publicar(empresa, html_path)

    print()
    print("─" * 50)
    print(f"  URL lista para enviar al cliente:")
    print(f"  {url}")
    print("─" * 50)
    print("  (Netlify tarda ~30 segundos en activar)")
