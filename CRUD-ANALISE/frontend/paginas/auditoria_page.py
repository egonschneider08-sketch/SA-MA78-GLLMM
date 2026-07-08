"""Página do domínio "Auditoria" — gerada a partir de registro.py."""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from registro import REGISTRO
from frontend.componentes import render_dominio

render_dominio("Auditoria", REGISTRO["Auditoria"])
