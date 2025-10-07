import datetime
import pandas as pd
import locale

# Define o locale para formatação de moeda (Brasil)
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

def formatar_data(data_obj):
    """Converte datetime.date para string yyyy-mm-dd"""
    if isinstance(data_obj, datetime.date):
        return data_obj.strftime("%Y-%m-%d")
    return ""

def validar_data_obj(data_obj):
    """Valida se é uma instância de datetime.date"""
    return isinstance(data_obj, datetime.date)

def formatar_mes_ref(data_obj):
    """Formata mês de referência como primeiro dia do mês"""
    if isinstance(data_obj, datetime.date):
        return datetime.date(data_obj.year, data_obj.month, 1).strftime("%Y-%m-%d")
    return ""

def validar_valor(valor_str):
    """Valida e converte valor para float com 2 casas decimais"""
    try:
        return round(float(str(valor_str).replace(",", ".").replace("R$", "").strip()), 2)
    except ValueError:
        return None

def formatar_valor(valor_float):
    """Formata valor float para string estilo R$ 1.000,00"""
    try:
        return locale.currency(valor_float, grouping=True)
    except Exception:
        return f"R$ {valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def carregar_excel(path):
    """Carrega arquivo Excel e retorna DataFrame"""
    try:
        df = pd.read_excel(path, engine="openpyxl")
        return df
    except Exception as e:
        print(f"Erro ao carregar Excel: {e}")
        return pd.DataFrame()

def gerar_opcoes_grupo():
    return [
        "Receitas", "Transferências", "Alimentos", "Advogado", "Cartão de Crédito",
        "Moradia", "Investimentos", "Tributos", "Reserva", "Extra", "Outros"
    ]

def gerar_opcoes_categoria():
    return [
            "Salário", 
            "Adiantamento",
            "13º salário",
            "Férias",
            "PLR / Bônus",
            "Freelance",
            "Doação", 
            "Empréstimo", 
            "Poupança", 
            "Medicamentos", 
            "Educação", 
            "Transporte", 
            "Venda", 
            "Ações", 
            "FII", 
            "Renda Fixa", 
            "Criptomoedas",
            "IPTU", 
            "IPVA", 
            "IRPF", 
            "Taxas Bancárias", 
            "Multas",
            "Vestuário", 
            "Presentes", 
            "Aluguel", 
            "Condomínio", 
            "Energia Elétrica", 
            "Água/Esgoto",
            "Gás",
            "Internet", 
            "Telefone/Celular", 
            "Mercado", 
            "Restaurantes", 
            "Lanches", 
            "Cafés", 
            "Farmácia", 
            "Plano de Saúde",
            "Consultas Médicas", 
            "Exames", 
            "Dentista", 
            "Combustível", 
            "Manutenção Veicular", 
            "SF880", 
            "Faxina", 
            "Limpeza/Manutenção", 
            "e-Social", 
            "Funcionários", 
            "Outros"
    ]

def gerar_opcoes_natureza():
    return ["Despesa", "Receita"]

def gerar_opcoes_tipo():
    return ["Fixo", "Variável"]

def gerar_opcoes_efetivado():
    return ["Sim", "Não"]