"""Página de consulta SQL livre (somente leitura)."""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd
from utils import execute_query

st.title("🛠️ Consulta SQL livre")
st.caption("Por segurança, apenas comandos SELECT são permitidos aqui.")

query = st.text_area(
    "SQL",
    height=140,
    placeholder="SELECT * FROM Cliente LIMIT 10",
)

if st.button("▶️ Executar"):
    if not query.strip().lower().startswith("select"):
        st.error("Por segurança, esse campo só aceita comandos SELECT.")
    else:
        try:
            registros = execute_query(query, fetch="all")
            if registros:
                st.dataframe(pd.DataFrame(registros), use_container_width=True)
                st.caption(f"{len(registros)} registro(s)")
            else:
                st.info("Consulta executada, nenhum resultado retornado.")
        except Exception as e:
            st.error(f"Erro na consulta: {e}")
