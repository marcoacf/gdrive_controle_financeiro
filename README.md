# Controle Financeiro

Este projeto tem como objetivo fornecer uma aplicação de controle financeiro pessoal utilizando Python, Streamlit e SQLite. Os dados são armazenados em um banco SQLite que pode ser sincronizado com o Google Drive para backup e acesso remoto. A interface é construída com Streamlit e oferece funcionalidades como:

- Autenticação simples
- Cadastro de lançamentos (CRUD)
- Consolidação mensal
- Avaliação por grupo
- Relatórios exportáveis (PDF/Excel)
- Dashboards interativos
- Carga de dados via Excel
- Controle de efetivações

## Estrutura do Projeto
```bash
controle_financeiro/
│
├── .venv/                      # Ambiente virtual
├── requirements.txt            # Dependências
├── config.py                   # Configurações (credenciais, usuários, etc)
├── bd_controle_fin.db          # Banco SQLite (sincronizado com Google Drive)
├── banco_de_dados.py           # Funções para manipular o banco
├── utils.py                    # Funções auxiliares
├── main.py                     # Interface principal com Streamlit
├── README.md                   # Documentação do projeto
├── pages/
│   ├── 1_crud.py               # Cadastro, edição e exclusão
│   ├── 2_consolidacao.py       # Consolidação mensal
│   ├── 3_grupo.py              # Avaliação por grupo
│   ├── 4_relatorio.py          # Relatórios exportáveis
│   ├── 5_dashboard.py          # Visualizações gráficas
│   ├── 6_carga_fria.py         # Importação de Excel
│   ├── 7_efetivacao.py         # Controle de efetivações
```

# ⚙️ Instalação e Configuração
## 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/controle_financeiro.git
cd controle_financeiro
```
## 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\\Scripts\\activate   # Windows
```
## 3. Instale as dependências
```bash
pip install -r requirements.txt
```
## 4. Configure o arquivo config.py
Inclua:
Usuários e senhas (com hash)
Credenciais da API do Google Drive (se for usar sincronização)
Parâmetros de segurança e personalização
```bash
USERS = {
    "marco": {
        "name": "Marco Antonio",
        "password": "hashed_password_aqui"
    }
}

GOOGLE_DRIVE_CONFIG = {
    "client_id": "...",
    "client_secret": "...",
    "refresh_token": "...",
    "folder_id": "ID_da_pasta_no_drive"
```

# ☁️ Publicação no GitHub e Streamlit Cloud
## 1. GitHub
Crie um repositório no GitHub
Suba o projeto:
```bash
git init
git add .
git commit -m "Primeiro commit"
git remote add origin https://github.com/seu-usuario/controle_financeiro.git
git push -u origin main
```

## 2. Streamlit Cloud
Acesse streamlit.io/cloud
Conecte sua conta GitHub
Escolha o repositório e o arquivo main.py
Configure variáveis de ambiente (se necessário)
Clique em Deploy

# ✅ Requisitos para rodar
* Python 3.8+
* Conta no Google (para Drive ou GCP)
* Conta no GitHub (para versionamento e publicação)
* Conta no Streamlit Cloud (para publicação online)