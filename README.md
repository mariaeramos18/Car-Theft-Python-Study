# 🚗 Vehicle Theft and Recovery Analysis (RJ - Brazil)

This project presents a visual and statistical analysis of **vehicle theft and recovery data** in the state of **Rio de Janeiro (Brazil)** from 2018 to 2023, using public data provided by the **ISP-RJ (Public Security Institute)**. The goal is to understand distribution trends and year-over-year averages using interactive visualizations.

---

## 📊 What It Does

- Loads public data from ISP-RJ
- Filters and trims outliers from vehicle theft and recovery reports
- Displays:
  - Boxplots of theft and recovery distributions (2018–2023)
  - Summary tables with **mean** and **standard deviation** per year

---

## 📦 Dataset

The dataset is sourced directly from:

**[ISP Dados RJ - BaseDPEvolucaoMensalCisp.csv](http://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv)**  
Encoding: `ISO-8859-1`  
Delimiter: `;`  
Decimal separator: `,`

Filtered columns used:
- `ano` (year)
- `roubo_veiculo` (vehicle theft)
- `recuperacao_veiculos` (vehicle recovery)

---

## 🛠️ Tech Stack

- Python 3
- pandas
- plotly
