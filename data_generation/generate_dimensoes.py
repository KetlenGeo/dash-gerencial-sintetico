# generate_dimensoes.py

import pandas as pd
import numpy as np
from config import *

def gerar_calendario():
    datas = pd.date_range(START_DATE, END_DATE, freq="D")
    df = pd.DataFrame({"Data": datas})
    df["Ano"] = df["Data"].dt.year
    df["Mes"] = df["Data"].dt.month
    df["AnoMes"] = df["Data"].dt.strftime("%Y%m")
    df["MesNome"] = df["Data"].dt.strftime("%B")
    df["DiaSemana"] = df["Data"].dt.weekday + 1
    return df

def gerar_empresa():
    return pd.DataFrame({
        "IdEmpresa": range(1, N_EMPRESAS + 1),
        "Empresa": [f"Empresa {i}" for i in range(1, N_EMPRESAS + 1)],
        "Matriz": np.random.choice(["BH", "SP", "RJ"], N_EMPRESAS)
    })

def gerar_cliente():
    return pd.DataFrame({
        "IdCliente": range(1, N_CLIENTES + 1),
        "Cliente": [f"Cliente {i}" for i in range(1, N_CLIENTES + 1)],
        "Segmento": np.random.choice(["Corporativo", "Publico", "Privado"], N_CLIENTES)
    })

def gerar_bem():
    return pd.DataFrame({
        "IdBem": range(1, N_BENS + 1),
        "TipoBem": np.random.choice(["Veiculo Leve", "Veiculo Pesado"], N_BENS),
        "DataAquisicao": pd.to_datetime(
            np.random.choice(pd.date_range("2015-01-01", "2021-12-31"), N_BENS)
        )
    })
