import streamlit as st

# === Variabili di partenza ===
nome_barman = "MirkoBot"
drink_speciale = "Digital Vodka"
quantità_drink_speciale = 28
alcolici = ["Mojito", "White Russian", "Caipirinha"]
analcolici = ["Limonata", "Coca Cola"]
prezzo_drink = 5.50
sconto_fedeltà = 1.50
cliente_preferito = "Sandro"
pub_aperto = True
consegna_domicilio_attiva = True

# === Titolo e introduzione ===
st.title("🍹 Pub Drink&Codice")
st.markdown(f"Benvenuto/a al Pub **Drink&Codice**! Sono **{nome_barman}** e sono pronto a servirti. 😉")

if pub_aperto:
    st.success("✅ Il pub è **aperto**!")

st.subheader("🥇 Il nostro drink speciale")
st.info(f"{drink_speciale} - solo {prezzo_drink} €")

st.markdown(f"**Drink disponibili:** {len(alcolici)} alcolici | {len(analcolici)} analcolici")

# === Input utente ===
nome_cliente = st.text_input("👤 Come ti chiami?")

if nome_cliente:
    st.markdown(f"Benvenuto/a **{nome_cliente}**!")

    anno_nascita = st.number_input("📅 In che anno sei nato?", min_value=1900, max_value=2025, step=1, format="%d")

    if anno_nascita > 0:
        anni_cliente = 2025 - anno_nascita
        st.write(f"Hai **{anni_cliente}** anni.")

        if anni_cliente < 18:
            st.warning("⚠️ Sei minorenne: puoi ordinare solo analcolici.")
            drink_disponibili = analcolici
        elif anni_cliente > 75:
            st.warning("👴 Sei in là con l'età, vai piano con gli alcolici!")
            drink_disponibili = alcolici + analcolici
        else:
            st.success("✅ Sei maggiorenne, puoi ordinare tutto!")
            drink_disponibili = alcolici + analcolici

        # Selezione drink
        drink_scelto = st.selectbox("🍸 Scegli il tuo drink:", options=drink_disponibili)

        if st.button("Ordina"):
            st.success(f"Hai scelto **{drink_scelto}**. Buon aperitivo! 🍻")

            if nome_cliente.lower() == cliente_preferito.lower() and anni_cliente >= 18:
                nuovo_prezzo = prezzo_drink - sconto_fedeltà
                st.info(f"🎉 Sei il nostro cliente preferito! Prezzo scontato: **{nuovo_prezzo} €**")
            else:
                st.info(f"💰 Il prezzo del drink è: **{prezzo_drink} €**")
