import streamlit as st
import pandas as pd
import plotly.express as px
from banco_de_dados import listar_lancamentos

st.set_page_config(page_title="Avaliação por Grupo", layout="wide")
st.title("📂 Avaliação por Grupo")

df = listar_lancamentos()

if df.empty:
    st.info("Nenhum lançamento encontrado.")
else:
    # Agrupa por grupo e natureza
    grupo_df = df.groupby(["grupo", "natureza"])["valor"].sum().reset_index()

    # Pivot para tabela com colunas Receita e Despesa
    tabela = grupo_df.pivot(index="grupo", columns="natureza", values="valor").fillna(0)
    tabela["Saldo"] = tabela.get("Receita", 0) - tabela.get("Despesa", 0)
    tabela = tabela.reset_index()

    st.subheader("📋 Tabela por Grupo")
    st.dataframe(tabela.style.format({
        "Receita": "R$ {:.2f}",
        "Despesa": "R$ {:.2f}",
        "Saldo": "R$ {:.2f}"
    }))

    st.subheader("📊 Gráfico de Grupos por Natureza")
    fig = px.bar(
        grupo_df, x="grupo", y="valor", color="natureza", barmode="group",
        labels={"grupo": "Grupo", "valor": "Valor (R$)", "natureza": "Natureza"},
        title="Receitas e Despesas por Grupo"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Gráfico de Saldo por Grupo")
    fig_saldo = px.bar(
        tabela, x="grupo", y="Saldo", color="Saldo",
        color_continuous_scale="RdYlGn",
        labels={"grupo": "Grupo", "Saldo": "Saldo (R$)"},
        title="Saldo por Grupo"
    )
    st.plotly_chart(fig_saldo, use_container_width=True)