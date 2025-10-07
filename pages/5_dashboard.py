import streamlit as st
import pandas as pd
import plotly.express as px
from banco_de_dados import listar_lancamentos

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")
st.title("📊 Dashboard Financeiro")

# Carrega os dados do banco de dados
df = listar_lancamentos()

if df.empty:
    st.info("Nenhum lançamento encontrado.")
else:
    # Converte data para datetime
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")

    # Gráfico de pizza por grupo
    st.subheader("🍕 Distribuição por Grupo")
    grupo_sum = df.groupby("grupo")["valor"].sum().reset_index()
    fig_grupo = px.pie(grupo_sum, names="grupo", values="valor", title="Distribuição de Valores por Grupo")
    st.plotly_chart(fig_grupo, use_container_width=True)

    # Gráfico de pizza por natureza
    st.subheader("🍕 Distribuição por Natureza")
    natureza_sum = df.groupby("natureza")["valor"].sum().reset_index()
    fig_natureza = px.pie(natureza_sum, names="natureza", values="valor", title="Distribuição de Valores por Natureza")
    st.plotly_chart(fig_natureza, use_container_width=True)

    # Evolução mensal
    st.subheader("📈 Evolução Mensal")
    evolucao = df.groupby(["mes_ref", "natureza"])["valor"].sum().reset_index()
    fig_evolucao = px.line(
        evolucao, x="mes_ref", y="valor", color="natureza", markers=True,
        labels={"mes_ref": "Mês de Referência", "valor": "Valor (R$)", "natureza": "Natureza"},
        title="Evolução Mensal de Receitas e Despesas"
    )
    st.plotly_chart(fig_evolucao, use_container_width=True)

    # Gráfico de barras por categoria
    st.subheader("📊 Valores por Categoria")
    categoria_sum = df.groupby("categoria")["valor"].sum().reset_index().sort_values(by="valor", ascending=False)
    fig_categoria = px.bar(
        categoria_sum, x="categoria", y="valor",
        labels={"categoria": "Categoria", "valor": "Valor (R$)"},
        title="Valores por Categoria"
    )
    st.plotly_chart(fig_categoria, use_container_width=True)