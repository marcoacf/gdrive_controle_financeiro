# Updated banco_de_dados.py to reflect DATE fields and proper formatting
import sqlite3
import pandas as pd
from config import LOCAL_DB_PATH

def conectar():
    return sqlite3.connect(LOCAL_DB_PATH)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lancamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grupo TEXT,
            natureza TEXT,
            tipo TEXT,
            data DATE,
            mes_ref DATE,
            categoria TEXT,
            descricao TEXT,
            parcela INTEGER,
            plano INTEGER,
            valor REAL,
            flag_efetivado TEXT,
            data_efetivado DATE
        )
    """)
    conn.commit()
    conn.close()

def inserir_lancamento(dados):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO lancamentos (
            grupo, natureza, tipo, data, mes_ref, categoria,
            descricao, parcela, plano, valor, flag_efetivado, data_efetivado
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, dados)
    conn.commit()
    conn.close()

def listar_lancamentos():
    conn = conectar()
    df = pd.read_sql_query("SELECT * FROM lancamentos", conn)
    conn.close()
    return df

def editar_lancamento(id, novos_dados):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE lancamentos SET
            grupo=?, natureza=?, tipo=?, data=?, mes_ref=?, categoria=?,
            descricao=?, parcela=?, plano=?, valor=?, flag_efetivado=?, data_efetivado=?
        WHERE id=?
    """, (*novos_dados, id))
    conn.commit()
    conn.close()

def excluir_lancamento(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lancamentos WHERE id=?", (id,))
    conn.commit()
    conn.close()