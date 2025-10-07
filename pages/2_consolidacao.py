import streamlit as st
import pandas as pd
import plotly.express as px
from banco_de_dados import listar_lancamentos

st.set_page_config(page_title="Consolidação Mensal", layout="wide")
st.title("📊 Consolidação por Mês de Referência")

# Carrega os lançamentos do banco de dados
df = listar_lancamentos()

if df.empty:
    st.info("Nenhum lançamento encontrado.")
else:
    # Agrupa por mês de referência e natureza (Receita/Despesa)
    consolidado = df.groupby(["mes_ref", "natureza"])["valor"].sum().reset_index()

    # Pivot para tabela com colunas Receita e Despesa
    tabela = consolidado.pivot(index="mes_ref", columns="natureza", values="valor").fillna(0)
    tabela["Saldo"] = tabela.get("Receita", 0) - tabela.get("Despesa", 0)
    tabela = tabela.reset_index()

    st.subheader("📋 Tabela Consolidada")
    st.dataframe(tabela.style.format({
        "Receita": "R$ {:.2f}",
        "Despesa": "R$ {:.2f}",
        "Saldo": "R$ {:.2f}"
    }))

    st.subheader("📈 Gráfico de Receita vs Despesa")
    fig = px.bar(
        consolidado, x="mes_ref", y="valor", color="natureza", barmode="group",
        labels={"mes_ref": "Mês de Referência", "valor": "Valor (R$)", "natureza": "Natureza"},
        title="Receitas e Despesas por Mês"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📉 Gráfico de Saldo Mensal")
    fig_saldo = px.line(
        tabela, x="mes_ref", y="Saldo", markers=True,
        labels={"mes_ref": "Mês de Referência", "Saldo": "Saldo (R$)"},
        title="Saldo por Mês"
    )
    st.plotly_chart(fig_saldo, use_container_width=True)