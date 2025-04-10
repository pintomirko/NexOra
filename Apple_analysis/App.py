import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === Funzione per pulizia colonne numeriche ===
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

# === Caricamento CSV ===
st.title("📊 Analisi Finanziaria Apple")

uploaded_file = st.file_uploader("Carica il file Apple.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';', engine='python', on_bad_lines='skip')

    # Mostra le prime righe
    st.subheader("Anteprima dati")
    st.dataframe(df.head())

    # Pulizia delle colonne principali
    colonne_da_pulire = [
        "Revenue (millions)", "Net Income (millions)", "EBITDA (millions)",
        "Gross Profit (millions)", "Op Income (millions)", "Total Assets (millions)",
        "Cash on Hand (millions)", "Long Term Debt (millions)", "Total Liabilities (millions)",
        "EPS", "PE ratio", "Gross Margin", "Employees"
    ]
    for col in colonne_da_pulire:
        if col in df.columns:
            pulisci_colonna(df, col)

    # Conversione anno
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce")
        df = df.sort_values("year")

    # Scelta colonna da visualizzare
    st.subheader("📈 Seleziona la colonna da analizzare")
    colonna = st.selectbox("Colonna numerica:", [col for col in colonne_da_pulire if col in df.columns])

    # Grafico
    st.subheader(f"Grafico per: {colonna}")
    fig, ax = plt.subplots()
    ax.plot(df["year"], df[colonna], marker='o')
    ax.set_title(f"Andamento di {colonna} nel tempo")
    ax.set_xlabel("Anno")
    ax.set_ylabel(colonna)
    ax.grid(True)
    st.pyplot(fig)
