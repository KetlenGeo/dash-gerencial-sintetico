# generate_fatos.py

import pandas as pd
import numpy as np
from config import *

def gerar_contratos(d_clientes, d_empresas):
    contratos = pd.DataFrame({
        "IdContrato": range(1, N_CONTRATOS + 1),
        "IdCliente": np.random.choice(d_clientes["IdCliente"], N_CONTRATOS),
        "IdEmpresa": np.random.choice(d_empresas["IdEmpresa"], N_CONTRATOS),
        "InicioContrato": pd.to_datetime(
            np.random.choice(pd.date_range("2021-01-01", "2023-01-01"), N_CONTRATOS)
        )
    })

    contratos["FimContrato"] = contratos["InicioContrato"] + pd.to_timedelta(
        np.random.randint(180, 900, N_CONTRATOS), unit="D"
    )

    contratos["StatusContrato"] = "Ativo"
    return contratos


def gerar_disponibilidade_diaria(d_contratos, d_bens):
    registros = []

    for _, contrato in d_contratos.iterrows():
        datas = pd.date_range(
            max(pd.to_datetime(START_DATE), contrato["InicioContrato"]),
            min(pd.to_datetime(END_DATE), contrato["FimContrato"]),
            freq="D"
        )

        bens = np.random.choice(d_bens["IdBem"], np.random.randint(1, 4), replace=False)

        for bem in bens:
            for data in datas:
                parado = np.random.rand() < PERC_INDISPONIBILIDADE
                registros.append([
                    data,
                    contrato["IdContrato"],
                    bem,
                    0 if parado else 1,
                    1 if parado else 0
                ])

    return pd.DataFrame(
        registros,
        columns=["Data", "IdContrato", "IdBem", "Ocupado", "ParadoManutencao"]
    )


def gerar_financeiro_mensal(d_contratos):
    registros = []

    for _, contrato in d_contratos.iterrows():
        meses = pd.period_range(
            contrato["InicioContrato"],
            contrato["FimContrato"],
            freq="M"
        )

        for mes in meses:
            registros.append([
                mes.strftime("%Y%m"),
                contrato["IdContrato"],
                np.random.normal(FATURAMENTO_MEDIO, DESVIO_FATURAMENTO),
                FATURAMENTO_MEDIO,
                np.random.uniform(0, 5_000),
                np.random.uniform(0, 3_000),
                np.random.uniform(0, 7_000)
            ])

    return pd.DataFrame(
        registros,
        columns=["AnoMes", "IdContrato", "Receita", "Meta", "Multas", "NotasDebito", "Pendencias"]
    )
