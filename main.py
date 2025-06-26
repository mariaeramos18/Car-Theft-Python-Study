# Library Imports
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data Import
df = pd.read_csv('http://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', encoding='ISO-8859-1', sep=';', decimal=',')

# Dashboard Layout
fig = make_subplots(
    subplot_titles=[
        'Vehicle Theft Distribution by Year',
        'Vehicle Recovery Distribution by Year',
        'Theft Statistics',
        'Recovery Statistics'
    ],
    rows=2,
    cols=2,
    specs=[[{'type': 'box'}, {'type': 'box'}], [{'type': 'table'}, {'type': 'table'}]]
)

# Column Selection
df_select = df[['ano', 'roubo_veiculo', 'recuperacao_veiculos']]

# Vehicle Theft Sample Selection
df_dist_roubo = df_select[(df_select['ano'] >= 2018) & (df_select['ano'] <= 2023)][['ano', 'roubo_veiculo']]
df_dist_roubo = df_dist_roubo[df_dist_roubo['roubo_veiculo'] <= df_dist_roubo['roubo_veiculo'].quantile(0.80)]

# Plot Theft Distribution
fig.add_trace(
    go.Box(x=df_dist_roubo['ano'], y=df_dist_roubo['roubo_veiculo']),
    row=1,
    col=1
)

# Vehicle Recovery Sample Selection
df_dist_rec = df_select[(df_select['ano'] >= 2018) & (df_select['ano'] <= 2023)][['ano', 'recuperacao_veiculos']]
df_dist_rec = df_dist_rec[df_dist_rec['recuperacao_veiculos'] <= df_dist_rec['recuperacao_veiculos'].quantile(0.90)]

# Plot Recovery Distribution
fig.add_trace(
    go.Box(x=df_dist_rec['ano'], y=df_dist_rec['recuperacao_veiculos']),
    row=1,
    col=2
)

# Theft Data Aggregation
df_stast_roubo = df_dist_roubo.groupby('ano').agg({'roubo_veiculo': ['mean', 'std']}).reset_index()

# Theft Statistics Table
fig.add_trace(
    go.Table(
        header=dict(
            values=['<b>YEAR</b>', '<b>MEAN</b>', '<b>STD DEV</b>'],
            line_color='white', fill_color='white',
            align='center', font=dict(color='black', size=12)
        ),
        cells=dict(
            values=[
                df_stast_roubo['ano'],
                round(df_stast_roubo['roubo_veiculo']['mean'], 3),
                round(df_stast_roubo['roubo_veiculo']['std'], 3)
            ]
        )
    ),
    row=2,
    col=1
)

# Recovery Data Aggregation
df_stast_rec = df_dist_rec.groupby('ano').agg({'recuperacao_veiculos': ['mean', 'std']}).reset_index()

# Recovery Statistics Table
fig.add_trace(
    go.Table(
        header=dict(
            values=['<b>YEAR</b>', '<b>MEAN</b>', '<b>STD DEV</b>'],
            line_color='white', fill_color='white',
            align='center', font=dict(color='black', size=12)
        ),
        cells=dict(
            values=[
                df_stast_rec['ano'],
                round(df_stast_rec['recuperacao_veiculos']['mean'], 3),
                round(df_stast_rec['recuperacao_veiculos']['std'], 3)
            ]
        )
    ),
    row=2,
    col=2
)

# Display the Dashboard
fig.show()
