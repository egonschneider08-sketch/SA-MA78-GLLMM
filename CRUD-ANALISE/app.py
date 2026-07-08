"""
app.py — ponto de entrada do site (Streamlit) do LuxeVoyage.

Rode a partir da pasta raiz do projeto:

    streamlit run app.py

Estrutura:
    registro.py            -> fonte única de verdade (domínio -> tabela -> metadados)
    frontend/componentes.py -> componentes de UI genéricos (Listar/Criar/Editar/Deletar)
    frontend/paginas/*.py   -> uma página por domínio + Dashboard + Consulta SQL

Cada página em frontend/paginas/ é "burra" de propósito: ela só busca o
domínio dela em REGISTRO e delega a renderização pra
frontend.componentes.render_dominio(). Toda a lógica de CRUD em si já
existe nos módulos de tabela (geografia/, clientes/, etc.) — o site não
duplica nada, só oferece outra forma de usar o mesmo backend do main.py.
"""
import streamlit as st

st.set_page_config(page_title="LuxeVoyage", page_icon="🧳", layout="wide")

paginas = {
    "Início": [
        st.Page("frontend/paginas/home_page.py", title="Dashboard", icon="🏠", default=True),
    ],
    "Domínios": [
        st.Page("frontend/paginas/geografia_page.py", title="Geografia", icon="🌎"),
        st.Page("frontend/paginas/parceiros_page.py", title="Parceiros", icon="🤝"),
        st.Page("frontend/paginas/catalogo_page.py", title="Catálogo", icon="🧳"),
        st.Page("frontend/paginas/clientes_page.py", title="Clientes", icon="👤"),
        st.Page("frontend/paginas/crm_page.py", title="CRM", icon="📈"),
        st.Page("frontend/paginas/comercial_page.py", title="Comercial", icon="💼"),
        st.Page("frontend/paginas/operacional_page.py", title="Operacional", icon="✈️"),
        st.Page("frontend/paginas/auditoria_page.py", title="Auditoria", icon="🛡️"),
    ],
    "Ferramentas": [
        st.Page("frontend/paginas/sql_page.py", title="Consulta SQL", icon="🛠️"),
    ],
}

pagina_atual = st.navigation(paginas)
pagina_atual.run()
