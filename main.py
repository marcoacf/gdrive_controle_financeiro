import streamlit as st
import bcrypt
from config import USERS

st.set_page_config(page_title="Controle Financeiro", layout="wide")

# Função de autenticação
def autenticar(usuario, senha):
    if usuario in USERS:
        senha_hash = USERS[usuario]["password"]
        return bcrypt.checkpw(senha.encode(), senha_hash)
    return False

# Sessão de autenticação
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔐 Login - Controle Financeiro")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar(usuario, senha):
            st.session_state.autenticado = True
            st.session_state.usuario = usuario
            st.success("Login realizado com sucesso!")
            #st.experimental_rerun()
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")
else:
    st.sidebar.title("📁 Navegação")
    st.sidebar.page_link("pages/1_crud.py", label="Cadastro de Lançamentos")
    st.sidebar.page_link("pages/2_consolidacao.py", label="Consolidação por Mês")
    st.sidebar.page_link("pages/3_grupo.py", label="Avaliação por Grupo")
    st.sidebar.page_link("pages/4_relatorio.py", label="Relatórios")
    st.sidebar.page_link("pages/5_dashboard.py", label="Dashboard")
    st.sidebar.page_link("pages/6_carga_fria.py", label="Carga Fria via Excel")
    st.sidebar.page_link("pages/7_efetivacao.py", label="Efetivação de Lançamentos")

    st.title("📊 Controle Financeiro")
    st.write(f"Bem-vindo, **{USERS[st.session_state.usuario]['name']}**! Use o menu lateral para navegar pelas funcionalidades.")