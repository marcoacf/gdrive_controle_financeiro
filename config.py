import bcrypt

# Usuários e senhas (hash gerado com bcrypt)
USERS = {
    "marcoacf": {
        "name": "Marco Cruz",
        "password": b"$2b$12$Jq2TSnEhO9PzsqYb579WZe8KTb0qD41LyYLby6NKsKxZOch3/BZ5i"  # exemplo de hash
    },
    "admin": {
        "name": "Administrador",
        "password": b"$2b$12$NJ5q4DIUsNvFPmepeIE7oOOYSg9MvLIBZvrU.Uh0PtNvqErTrU/V2"  # exemplo de hash
    }
}

# Configuração da API do Google Drive
GOOGLE_DRIVE_CONFIG = {
    "client_id": "SEU_CLIENT_ID",
    "client_secret": "SEU_CLIENT_SECRET",
    "refresh_token": "SEU_REFRESH_TOKEN",
    "folder_id": "ID_DA_PASTA_NO_DRIVE"
}

# Caminho local do banco de dados
LOCAL_DB_PATH = "bd_controle_fin.db"

# Nome do arquivo no Google Drive
DRIVE_DB_FILENAME = "bd_controle_fin.db"