# Pub Drink&Codice


# Dichiarazione variabili

nome_barman = "MirkoBot"
drink_speciale = "Digital Vodka"
quantità_drink_speciale = 28
alcolici = ["Mojito", "White Russian", "Caipirinha"]
analcolici = ["Limonata", "Coca Cola"]
drink_disponibili = alcolici + analcolici
prezzo_drink = 5.50
sconto_fedeltà = 1.50
cliente_preferito = "Sandro"
pub_aperto = True
consegna_domicilio_attiva = True


# Inizio del programma

print("\nBenvenuto/a al Pub Drink&Codici 🍻")
if pub_aperto:
    print("Siamo aperti!")
print("Mi chiamo "+nome_barman+"... e sono pronto a servirti! 😉")

print("\nIl drink più cool del nostro pub è: " + str(drink_speciale))
print("Provalo subito al prezzo di " + str(prezzo_drink) + " euro")

print("\nI drink alcolici a disposizione al momento sono " + str(len(alcolici)) + ", quelli analcolici " + str(len(analcolici)))

print("\nCome ti chiami? ")
nome_cliente = input()

print("\nBenvenuto/a " + str(nome_cliente))

anno_nascita = int(input("\nIn che anno sei nato? "))
anni_cliente = 2025 - anno_nascita
print("Quindi hai " + str(anni_cliente) + " anni")
if anni_cliente < 18:
    print("Sei minorenne: puoi ordinare solo analcolici")
    drink_disponibili = analcolici
elif anni_cliente > 75:
    print("Sei in là con l'età, stai attento")
else:
    print("Sei maggiorenne: puoi ordinare alcolici ed analcolici")
    drink_disponibili = alcolici + analcolici
while True:
    print("\nEcco i drink disponibili questa sera: ")
    for x in drink_disponibili:
        print(x)

    drink_scelto = input("\nQuale bevanda preferisci? ")
    if drink_scelto in drink_disponibili:
        print("\nHai scelto " +drink_scelto+ ". Buon aperitivo! 🍻")
        break
    else:
        print("\nMi dispiace, il drink " +drink_scelto+ " non è disponibile. 😕")

if nome_cliente == cliente_preferito and anni_cliente >= 18:
    nuovo_prezzo_drink = prezzo_drink - sconto_fedeltà
    print("C'è un piccolo sconto per te! Il prezzo finale è " + str(nuovo_prezzo_drink) + " euro")
else:
    print("Il prezzo è di 5.5 euro")
