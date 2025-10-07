import streamlit as st
import pandas as pd
from datetime import datetime
from banco_de_dados import inserir_lancamento, criar_tabela
from utils import validar_valor

st.set_page_config(page_title="Carga Fria de Lançamentos", layout="wide")
st.title("📥 Carga Fria de Lançamentos via Excel")

criar_tabela()

uploaded_file = st.file_uploader("Selecione o arquivo Excel (.xlsx)", type=["xlsx"])

def parse_date(value):
    if pd.isna(value):
        return None
    if isinstance(value, datetime):
        return value.date()
    try:
        return datetime.strptime(str(value), "%d/%m/%Y").date()
    except ValueError:
        return None

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.subheader("📋 Pré-visualização dos dados")
        st.dataframe(df)

        colunas_necessarias = [
            "grupo", "natureza", "tipo", "data", "mes_ref", "categoria",
            "descricao", "parcela", "plano", "valor", "flag_efetivado", "data_efetivado"
        ]
        if not all(col in df.columns for col in colunas_necessarias):
            st.error("O arquivo Excel deve conter todas as colunas obrigatórias.")
        else:
            erros = []
            for i, row in df.iterrows():
                data = parse_date(row["data"])
                mes_ref = parse_date(row["mes_ref"])
                data_efetivado = parse_date(row["data_efetivado"])
                valor = validar_valor(str(row["valor"]))

                if data is None:
                    erros.append(f"Linha {i+2}: Data do lançamento inválida.")
                if mes_ref is None:
                    erros.append(f"Linha {i+2}: Mês de referência inválido.")
                if row["flag_efetivado"] == "Sim" and data_efetivado is None:
                    erros.append(f"Linha {i+2}: Data de efetivação inválida.")
                if valor is None:
                    erros.append(f"Linha {i+2}: Valor inválido.")

            if erros:
                st.warning("⚠️ Erros encontrados na validação:")
                for erro in erros:
                    st.text(erro)
            else:
                if st.button("✅ Importar lançamentos para o banco"):
                    for _, row in df.iterrows():
                        dados = (
                            row["grupo"], row["natureza"], row["tipo"],
                            parse_date(row["data"]).strftime("%Y-%m-%d"),
                            parse_date(row["mes_ref"]).strftime("%Y-%m-%d"),
                            row["categoria"], row["descricao"],
                            int(row["parcela"]), int(row["plano"]),
                            validar_valor(str(row["valor"])),
                            row["flag_efetivado"],
                            parse_date(row["data_efetivado"]).strftime("%Y-%m-%d") if row["flag_efetivado"] == "Sim" else None
                        )
                        inserir_lancamento(dados)
                    st.success("Lançamentos importados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")