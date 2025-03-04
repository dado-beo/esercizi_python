import random
#1. Popolamento statico iniziale:
dizionario = {
    "Mario Rossi" : [((8, 7, 9), "Junior Chef"), ((7, 8, 8), "Junior Chef"), ((9, 9, 8), "Junior Chef"), ((8, 8, 9), "Junior Chef")],
    "Luigi Bianchi" : [((7, 7, 8), "Senior Chef"), ((8, 9, 7), "Senior Chef"), ((7, 8, 7), "Senior Chef"), ((9, 8, 8), "Senior Chef")],
    "Giulia Verdi" : [((9, 8, 8), "Junior Chef"), ((8, 7, 9), "Junior Chef"), ((8, 8, 8), "Junior Chef"), ((7, 9, 8), "Junior Chef")],
}
listaCategoriaPiatti = ["Antipasti", "Primi", "Secondi", "Dessert", "Piatti unici"] # Dichiaro le varie categorie

#2. Aggiunta statica di un nuovo chef:
dizionario["Davide Beolchi"] = [((8, 7, 9), "Junior Chef"), ((7, 3, 8), "Junior Chef"), ((9, 9, 8), "Junior Chef"), ((8, 8, 9), "Junior Chef")]

#3. Funzione per l'aggiunta di una nuova categoria di piatto:
def funzioneAggiuntaCetegoria():
    for lista, in dizionario.values():
        for dati, nome in lista:
            creatività = random.randint(1,10)
            gusto = random.randint(1,10)
            presentazione = random.randint(1,10)
            if(nome == "Junior Chef"):
                dizionario[lista] = ((creatività, gusto, presentazione),"Junior Chef")
            else:
                dizionario[lista] = ((creatività, gusto, presentazione),"Senior Chef")
#funzioneAggiuntaCetegoria()
print(dizionario)

#4. Funzione per la stampa dati di uno chef :
def mostraChef(nomeChef):
    print(f"Ecco i dati dello chef {nomeChef}:")
    i = 0
    for dati in dizionario[nomeChef]:
        valori, categoria = dati
        (punteggi1, punteggi2, punteggi3) = valori
        print(f"Categoria {listaCategoriaPiatti[i]}: ")
        print(f"Categoria di chef: {categoria}")
        print(f"Punteggi antipasti :{punteggi1}")
        print(f"creatività: {punteggi2}")
        print(f"Gusto: {punteggi3}")
    i += 1
nomeChef = input("Inserisci il nome dello chef: ")
if(nomeChef not in dizionario):
    print("Errore! Chef non presente.")
else:
    mostraChef(nomeChef)

#5. Funzione per la stampa dati di un piatto:
def stampaPiatto(categoriaPiattiPosizione):
    pass

categoriaPiatti = input("Inserisci la categoria dei piatti: ")
if(categoriaPiatti not in listaCategoriaPiatti):
    print("Errore! Categoria non presente.")
else:
    if(categoriaPiatti == "Antipasti"):
        categoriaPiattiPosizione = 0
    elif(categoriaPiatti == "Primi"):
        categoriaPiattiPosizione = 1
    elif(categoriaPiatti == "Secondi"):
        categoriaPiattiPosizione = 2
    elif(categoriaPiatti == "Dessert"):
        categoriaPiattiPosizione = 3
    elif(categoriaPiatti == "Piatti unici"):
        categoriaPiattiPosizione = 4 
    stampaPiatto(categoriaPiattiPosizione)

#6. Funzione per l'analisi dei punteggi:

#7. Funzione per l'aggiunta di un nuovo chef:
def inserisci_nuovo_chef(dizionario, nominativo, risultati):
    dizionario[nominativo] = risultati

def inserisci_dati_nuovo_chef():
    listaRisultati = []
    i = 0
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    nomeCognome = nome +" "+ cognome
    if(nomeCognome in dizionario):
        print("Nome già presente! ")
    else:    
        while(len(listaCategoriaPiatti) > i):
            print(f"Categoria {listaCategoriaPiatti[i]}: ")
            punteggio1 = input("Inserisci il punteggio 1:")
            punteggio2 = input("Inserisci il punteggio 2:")
            punteggio3 = input("Inserisci il punteggio 3:")

            categoria = input("Inserisci la categoria: ")

            listaRisultati.append((punteggio1, punteggio2, punteggio3), categoria)
            i += 1
    return nomeCognome, listaRisultati
nominativo, risultati = inserisci_dati_nuovo_chef()
inserisci_nuovo_chef(dizionario, nominativo, risultati)