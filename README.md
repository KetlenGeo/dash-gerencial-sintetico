# Dashboard Gerencial com Dados Sintéticos
Este projeto demonstra a construção de um ambiente analítico completo a partir da **geração de dados sintéticos em Python**, simulando um contexto corporativo real, com foco em **consumo gerencial via Power BI**.
O objetivo é apresentar não apenas visualização de dados, mas todo o raciocínio por trás da **modelagem, regras de negócio e estruturação das bases**.

---

## Objetivo do Projeto
- Simular um ambiente corporativo real com múltiplas áreas de negócio
- Gerar dados sintéticos coerentes e reprodutíveis via Python
- Criar bases prontas para consumo analítico em Power BI
- Viabilizar um dashboard gerencial totalmente interativo, sem uso de dados sensíveis

---

## Contexto Analítico
O projeto simula uma organização com indicadores das seguintes áreas:
- **Operações** (frota, ocupação, disponibilidade e manutenção)
- **Financeiro** (faturamento, metas e pendências)
- **Vendas** (volume e ticket médio)
- **Customer Service** (NPS, retorno e chamados)

Os dados foram gerados respeitando regras de negócio realistas, como:
- Histórico de **3 anos**
- **600 bens** (ativos)
- Indisponibilidade média de **8%**
- Faturamento mensal **estável**
- NPS com **perfil realista**

---

## Arquitetura do Projeto
### Estrutura do Repositório

dash-gerencial-sintetico/
│
├── config.py
├── main.py
├── README.md
│
└── data_generation/
├── generate_dimensoes.py
├── generate_fatos.py


### Descrição dos Arquivos
- **config.py**  
  Centraliza os parâmetros do negócio (volumes, períodos, percentuais e distribuições).

- **generate_dimensoes.py**  
  Responsável pela geração das tabelas dimensão (calendário, empresa, cliente, bens, contratos).

- **generate_fatos.py**  
  Responsável pela geração das tabelas fato, respeitando granularidade e regras de negócio.

- **main.py**  
  Orquestra a execução do projeto e exporta os dados finais para Excel.

---

## Modelo de Dados
O modelo segue o padrão **estrela**, com:

### Dimensões
- dCalendario  
- dEmpresa  
- dCliente  
- dBem  
- dContrato  

### Fatos
- fDisponibilidadeDiaria  
- fFinanceiroMensal  
- fVendas  
- fCustomerService  
As tabelas foram pensadas para suportar análises temporais, operacionais e gerenciais de forma integrada.

---

## Tecnologias Utilizadas
- Python
- Pandas
- NumPy
- OpenPyXL
- Power BI

---

## Observação Importante
Todos os dados utilizados neste projeto são 100% sintéticos, não representando informações reais de nenhuma empresa, cliente ou contrato.
O foco do projeto está na estrutura, modelagem e raciocínio analítico, e não nos dados em si.
