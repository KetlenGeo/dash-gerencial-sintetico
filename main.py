# main.py

import numpy as np
import pandas as pd

from config import SEED
from generate_dimensoes import *
from generate_fatos import *

np.random.seed(SEED)

dCalendario = gerar_calendario()
dEmpresa = gerar_empresa()
dCliente = gerar_cliente()
dBem = gerar_bem()

dContrato = gerar_contratos(dCliente, dEmpresa)
fDisponibilidade = gerar_disponibilidade_diaria(dContrato, dBem)
fFinanceiro = gerar_financeiro_mensal(dContrato)

with pd.ExcelWriter("output/dados_sinteticos.xlsx", engine="openpyxl") as writer:
    dCalendario.to_excel(writer, sheet_name="dCalendario", index=False)
    dEmpresa.to_excel(writer, sheet_name="dEmpresa", index=False)
    dCliente.to_excel(writer, sheet_name="dCliente", index=False)
    dBem.to_excel(writer, sheet_name="dBem", index=False)
    dContrato.to_excel(writer, sheet_name="dContrato", index=False)
    fDisponibilidade.to_excel(writer, sheet_name="fDisponibilidadeDiaria", index=False)
    fFinanceiro.to_excel(writer, sheet_name="fFinanceiroMensal", index=False)
