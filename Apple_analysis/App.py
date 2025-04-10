import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def pulisci_colonna(df, nome_colonna):
    df[nome_colonna] = (
        df[nome_colonna]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace("%", "", regex=False)
        .str.strip()
    )
    df[nome_colonna] = pd.to_numeric(df[nome_colonna], errors="coerce")

url = "https://raw.githubusercontent.com/pintomirko/NexOra/main/Apple_analysis/Apple.csv"
df = pd.read_csv(url, sep=";", engine="python", on_bad_lines="skip")

st.title("📊 Analisi Finanziaria Apple")
st.subheader("Anteprima dati")
st.dataframe(df.head())

colonne_da_pulire = [
    "Revenue (millions)", "Net Income (millions)", "EBITDA (millions)",
    "Gross Profit (millions)", "Op Income (millions)", "Total Assets (millions)",
    "Cash on Hand (millions)", "Long Term Debt (millions)", "Total Liabilities (millions)",
    "EPS", "PE ratio", "Gross Margin", "Employees"
]
for col in colonne_da_pulire:
    if col in df.columns:
        pulisci_colonna(df, col)

if "year" in df.columns:
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df = df.sort_values("year")

st.subheader("📈 Seleziona la colonna da analizzare")
colonna = st.selectbox("Colonna numerica:", [col for col in colonne_da_pulire if col in df.columns])

st.subheader(f"Grafico per: {colonna}")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(df["year"], df[colonna], marker='o')
ax.set_xlabel("Anno")
ax.set_ylabel(colonna)
ax.set_title(f"Andamento di {colonna}")
ax.grid(True)
st.pyplot(fig)
