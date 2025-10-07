import streamlit as st
import pandas as pd
from banco_de_dados import listar_lancamentos, editar_lancamento

st.set_page_config(page_title="Efetivação de Lançamentos", layout="wide")
st.title("✅ Controle de Efetivações")

# Carrega os dados do banco
df = listar_lancamentos()

if df.empty:
    st.info("Nenhum lançamento encontrado.")
else:
    # Filtra lançamentos não efetivados
    df_nao_efetivados = df[df["flag_efetivado"].str.upper() == "N"]

    st.subheader("🔍 Lançamentos Não Efetivados")
    st.dataframe(df_nao_efetivados)

    # Filtros
    st.sidebar.header("Filtros")
    grupos = st.sidebar.multiselect("Grupo", options=sorted(df_nao_efetivados["grupo"].unique()), default=list(df_nao_efetivados["grupo"].unique()))
    categorias = st.sidebar.multiselect("Categoria", options=sorted(df_nao_efetivados["categoria"].unique()), default=list(df_nao_efetivados["categoria"].unique()))
    mes_ref = st.sidebar.multiselect("Mês de Referência", options=sorted(df_nao_efetivados["mes_ref"].unique()), default=list(df_nao_efetivados["mes_ref"].unique()))

    df_filtrado = df_nao_efetivados[
        (df_nao_efetivados["grupo"].isin(grupos)) &
        (df_nao_efetivados["categoria"].isin(categorias)) &
        (df_nao_efetivados["mes_ref"].isin(mes_ref))
    ]

    st.subheader("📋 Lançamentos Filtrados para Efetivação")
    st.dataframe(df_filtrado)

    # Seleção de lançamento para efetivar
    if not df_filtrado.empty:
        st.subheader("✏️ Marcar como Efetivado")
        id_selecionado = st.selectbox("Selecione o ID do lançamento", df_filtrado["id"])
        data_efetivacao = st.date_input("Data de Efetivação")

        if st.button("Confirmar Efetivação"):
            lancamento = df[df["id"] == id_selecionado].iloc[0]
            novos_dados = (
                lancamento["grupo"], lancamento["natureza"], lancamento["tipo"],
                lancamento["data"], lancamento["mes_ref"], lancamento["categoria"],
                lancamento["descricao"], lancamento["parcela"], lancamento["plano"],
                lancamento["valor"], "S", data_efetivacao.strftime("%d/%m/%Y")
            )
            editar_lancamento(id_selecionado, novos_dados)
            st.success(f"Lançamento ID {id_selecionado} marcado como efetivado.")