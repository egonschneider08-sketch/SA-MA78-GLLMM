"""
frontend/componentes.py — componentes de UI reutilizáveis (Streamlit).

Um único conjunto de funções genéricas que sabe renderizar Listar / Criar /
Buscar-Editar / Deletar / Buscar-por-campo para QUALQUER tabela do
registro.py — a mesma ideia do menu de terminal (main.py), só que em HTML.

Nenhuma página de domínio (frontend/paginas/*.py) precisa reimplementar
essa lógica: elas só chamam render_dominio(nome, tabelas).
"""
import streamlit as st
import pandas as pd


def _chamar(mod, nome_funcao, *args, **kwargs):
    """Wrapper com tratamento de erro amigável pra qualquer chamada ao backend."""
    try:
        funcao = getattr(mod, nome_funcao)
        return funcao(*args, **kwargs), None
    except Exception as e:
        return None, str(e)


def _aba_listar(info):
    col1, col2 = st.columns(2)
    limit = col1.number_input("Limite", min_value=1, max_value=1000, value=50,
                               key=f"limit_{info['entidade']}")
    offset = col2.number_input("Offset", min_value=0, value=0,
                                key=f"offset_{info['entidade']}")
    if st.button("🔄 Atualizar lista", key=f"listar_{info['entidade']}"):
        registros, erro = _chamar(info["mod"], f"listar_{info['plural']}",
                                   limit=int(limit), offset=int(offset))
        if erro:
            st.error(erro)
        elif registros:
            st.dataframe(pd.DataFrame(registros), use_container_width=True)
            st.caption(f"{len(registros)} registro(s)")
        else:
            st.info("Nenhum registro encontrado.")


def _aba_criar(info):
    with st.form(key=f"form_criar_{info['entidade']}"):
        valores = [st.text_input(col, key=f"criar_{info['entidade']}_{col}")
                   for col in info["cols"]]
        enviado = st.form_submit_button("➕ Criar")
    if enviado:
        novo_id, erro = _chamar(info["mod"], f"criar_{info['entidade']}", *valores)
        if erro:
            st.error(erro)
        else:
            st.success(f"Registro criado com sucesso! id gerado: {novo_id}")


def _aba_buscar_editar(info):
    id_valor = st.text_input(f"{info['pk']}", key=f"buscar_id_{info['entidade']}")
    chave_estado = f"registro_atual_{info['entidade']}"

    if st.button("🔍 Buscar", key=f"btn_buscar_{info['entidade']}") and id_valor:
        registro, erro = _chamar(info["mod"], f"buscar_{info['entidade']}_por_id", id_valor)
        if erro:
            st.error(erro)
        elif registro:
            st.session_state[chave_estado] = registro
        else:
            st.session_state.pop(chave_estado, None)
            st.warning("Nenhum registro encontrado com esse id.")

    registro_atual = st.session_state.get(chave_estado)
    if registro_atual:
        st.dataframe(pd.DataFrame([registro_atual]), use_container_width=True)
        st.markdown("**Editar campos** (deixe em branco para não alterar):")
        with st.form(key=f"form_editar_{info['entidade']}"):
            novos_valores = {}
            for col in info["cols"]:
                valor_atual = registro_atual.get(col, "")
                novos_valores[col] = st.text_input(
                    col,
                    value="" if valor_atual is None else str(valor_atual),
                    key=f"editar_{info['entidade']}_{col}",
                )
            salvar = st.form_submit_button("💾 Salvar alterações")
        if salvar:
            campos = {k: v for k, v in novos_valores.items() if v != ""}
            if not campos:
                st.info("Nenhum campo alterado.")
            else:
                linhas, erro = _chamar(info["mod"], f"atualizar_{info['entidade']}",
                                        id_valor, **campos)
                if erro:
                    st.error(erro)
                else:
                    st.success(f"Atualizado! Linhas afetadas: {linhas}")

        st.divider()
        if st.checkbox("Quero excluir este registro", key=f"chk_deletar_{info['entidade']}"):
            st.warning(f"Confirma a exclusão do id {id_valor}? Essa ação não pode ser desfeita.")
            if st.button("🗑️ Confirmar exclusão", key=f"btn_deletar_{info['entidade']}"):
                linhas, erro = _chamar(info["mod"], f"deletar_{info['entidade']}", id_valor)
                if erro:
                    st.error(erro)
                else:
                    st.success(f"Excluído. Linhas afetadas: {linhas}")
                    st.session_state.pop(chave_estado, None)


def _aba_buscar_por_campo(info):
    campo = st.selectbox("Campo", [info["pk"]] + info["cols"],
                          key=f"campo_{info['entidade']}")
    valor = st.text_input("Valor", key=f"valor_{info['entidade']}")
    if st.button("🔎 Buscar", key=f"btn_buscar_campo_{info['entidade']}"):
        registros, erro = _chamar(info["mod"], f"buscar_{info['plural']}_por_campo", campo, valor)
        if erro:
            st.error(erro)
        elif registros:
            st.dataframe(pd.DataFrame(registros), use_container_width=True)
            st.caption(f"{len(registros)} registro(s)")
        else:
            st.info("Nenhum registro encontrado.")


def render_tabela(nome_tabela, info):
    """Renderiza a UI completa (4 abas) de uma única tabela."""
    st.markdown(f"## {nome_tabela}")
    aba1, aba2, aba3, aba4 = st.tabs(
        ["📋 Listar", "➕ Criar", "🔍 Buscar / Editar / Deletar", "🔎 Buscar por campo"]
    )
    with aba1:
        _aba_listar(info)
    with aba2:
        _aba_criar(info)
    with aba3:
        _aba_buscar_editar(info)
    with aba4:
        _aba_buscar_por_campo(info)


def render_dominio(nome_dominio, tabelas):
    """
    Renderiza uma página de domínio inteira: um seletor de tabela
    + a UI de CRUD da tabela escolhida.
    """
    st.title(nome_dominio)
    nomes = list(tabelas.keys())
    escolha = st.selectbox("Tabela", nomes, key=f"select_tabela_{nome_dominio}")
    render_tabela(escolha, tabelas[escolha])
