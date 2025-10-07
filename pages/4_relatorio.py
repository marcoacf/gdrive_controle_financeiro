import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import date
from banco_de_dados import listar_lancamentos

st.set_page_config(page_title="Relatórios Detalhados", layout="wide")
st.title("📄 Relatórios Detalhados")

# Carrega os dados do banco de dados
df = listar_lancamentos()

if df.empty:
    st.info("Nenhum lançamento encontrado.")
else:
    # Converte campos de data para datetime
    df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d", errors="coerce")
    df["mes_ref"] = pd.to_datetime(df["mes_ref"], format="%Y-%m-%d", errors="coerce")
    df["data_efetivado"] = pd.to_datetime(df["data_efetivado"], format="%Y-%m-%d", errors="coerce")

    # Filtros
    st.sidebar.header("🔎 Filtros")
    grupos = st.sidebar.multiselect("Grupo", options=sorted(df["grupo"].dropna().unique()), default=list(df["grupo"].dropna().unique()))
    naturezas = st.sidebar.multiselect("Natureza", options=sorted(df["natureza"].dropna().unique()), default=list(df["natureza"].dropna().unique()))
    categorias = st.sidebar.multiselect("Categoria", options=sorted(df["categoria"].dropna().unique()), default=list(df["categoria"].dropna().unique()))
    data_inicio = st.sidebar.date_input("Data inicial", value=df["data"].min().date() if not df["data"].isna().all() else date.today())
    data_fim = st.sidebar.date_input("Data final", value=df["data"].max().date() if not df["data"].isna().all() else date.today())

    # Aplica os filtros
    df_filtrado = df[
        (df["grupo"].isin(grupos)) &
        (df["natureza"].isin(naturezas)) &
        (df["categoria"].isin(categorias)) &
        (df["data"] >= pd.to_datetime(data_inicio)) &
        (df["data"] <= pd.to_datetime(data_fim))
    ]

    st.subheader("📋 Lançamentos Filtrados")
    st.dataframe(df_filtrado)

    # Exportação para Excel
    def gerar_excel(dataframe):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            dataframe.to_excel(writer, index=False, sheet_name='Relatório')
        output.seek(0)
        return output

    st.download_button(
        label="📥 Exportar para Excel",
        data=gerar_excel(df_filtrado),
        file_name="relatorio_lancamentos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )