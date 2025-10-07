import streamlit as st
from banco_de_dados import criar_tabela, inserir_lancamento, listar_lancamentos, editar_lancamento, excluir_lancamento
from utils import (
    gerar_opcoes_grupo, gerar_opcoes_natureza, gerar_opcoes_tipo,
    gerar_opcoes_efetivado, validar_valor, formatar_valor
)

st.set_page_config(page_title="Cadastro de Lançamentos", layout="wide")
st.title("📋 Cadastro de Lançamentos")

criar_tabela()

# Formulário de cadastro
with st.form("form_lancamento"):
    col1, col2, col3 = st.columns(3)
    grupo = col1.selectbox("Grupo", gerar_opcoes_grupo())
    natureza = col2.selectbox("Natureza", gerar_opcoes_natureza())
    tipo = col3.selectbox("Tipo", gerar_opcoes_tipo())

    col4, col5, col6 = st.columns(3)
    data = col4.date_input("Data do lançamento")
    mes_ref = col5.date_input("Mês de referência")
    categoria = col6.text_input("Categoria")

    descricao = st.text_input("Descrição")
    
    col7, col8, col9 = st.columns(3)
    parcela = col7.number_input("Parcela", min_value=1, step=1)
    plano = col8.number_input("Plano de Parcelamento", min_value=1, step=1)
    valor = col9.text_input("Valor (ex: R$ 1.000,00)")

    col10, col11 = st.columns(2)
    flag_efetivado = col10.selectbox("Efetivado?", gerar_opcoes_efetivado())
    data_efetivado = col11.date_input("Data Efetivação")

    submitted = st.form_submit_button("Salvar Lançamento")

    if submitted:
        if flag_efetivado == "Sim" and data_efetivado is None:
            st.error("Data de efetivação inválida.")
        elif validar_valor(valor) is None:
            st.error("Valor inválido. Use o formato R$ 1.000,00.")
        else:
            dados = (
                grupo, natureza, tipo,
                data.strftime("%Y-%m-%d"),
                mes_ref.strftime("%Y-%m-%d"),
                categoria, descricao,
                parcela, plano,
                validar_valor(valor),
                flag_efetivado,
                data_efetivado.strftime("%Y-%m-%d") if flag_efetivado == "Sim" else None
            )
            inserir_lancamento(dados)
            st.success("Lançamento salvo com sucesso!")

# Listagem e edição
st.subheader("🔍 Lançamentos cadastrados")
df = listar_lancamentos()

if not df.empty:
    st.dataframe(df)

    with st.expander("✏️ Editar ou Excluir"):
        id_selecionado = st.selectbox("Selecione o ID para editar/excluir", df["id"])
        dados_atual = df[df["id"] == id_selecionado].iloc[0]

        novo_valor = st.text_input("Novo valor", value=formatar_valor(dados_atual["valor"]))
        nova_descricao = st.text_input("Nova descrição", value=dados_atual["descricao"])
        acao = st.radio("Ação", ["Editar", "Excluir"])

        if st.button("Confirmar"):
            if acao == "Editar":
                valor_float = validar_valor(novo_valor)
                if valor_float is None:
                    st.error("Valor inválido.")
                else:
                    novos_dados = (
                        dados_atual["grupo"], dados_atual["natureza"], dados_atual["tipo"],
                        dados_atual["data"], dados_atual["mes_ref"], dados_atual["categoria"],
                        nova_descricao, dados_atual["parcela"], dados_atual["plano"],
                        valor_float, dados_atual["flag_efetivado"], dados_atual["data_efetivado"]
                    )
                    editar_lancamento(id_selecionado, novos_dados)
                    st.success("Lançamento editado com sucesso.")
            else:
                excluir_lancamento(id_selecionado)
                st.success("Lançamento excluído com sucesso.")
else:
    st.info("Nenhum lançamento cadastrado ainda.")