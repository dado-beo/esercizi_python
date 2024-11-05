

dati_Pluviometrici = (("Bergamo", [("Gennaio", 100),("Febbraio", "N/D"),("Marzo", 102),("Aprile", "N/D"),("Maggio", 104),("Giugno", 105),("Luglio", 106),("Agosto", 107),("Settembre", 108),("Ottobre", 109),("Novembre", 110),("Dicembre", 111)]),
("Brescia", [("Gennaio", 90),("Febbraio", "N/D"),("Marzo", 92),("Aprile", 93),("Maggio", 94),("Giugno", 95),("Luglio", 96),("Agosto", 97),("Settembre", 98),("Ottobre", 99),("Novembre", 100),("Dicembre", 101)]),
("Como", [("Gennaio", 80),("Febbraio", 81),("Marzo", 82),("Aprile", "N/D"),("Maggio", 84),("Giugno", 85),("Luglio", 86),("Agosto", 87),("Settembre", 88),("Ottobre", 89),("Novembre", 90),("Dicembre", 91)]),
("Cremona", [("Gennaio", 70),("Febbraio", 71),("Marzo", 72),("Aprile", 73),("Maggio", 74),("Giugno", 75),("Luglio", "N/D"),("Agosto", 77),("Settembre", 78),("Ottobre", 79),("Novembre", 80),("Dicembre", 81)]),
("Lecco", [("Gennaio", "N/D"),("Febbraio", "N/D"),("Marzo", "N/D"),("Aprile", "N/D"),("Maggio", "N/D"),("Giugno", "N/D"),("Luglio", "N/D"),("Agosto", "N/D"),("Settembre", "N/D"),("Ottobre", "N/D"),("Novembre", "N/D"),("Dicembre", "N/D")]))

listaMesiMax = []
listaMesiMin = []

def datiTuaCittà(nome): 
    sommaValori = 0
    contatore = 0
    contatoreND = 0
    for città, *dati in dati_Pluviometrici:
        if(città == nome):
            for i in dati: 
                for mese, valore in i:
                    # Inizializzazione val max/min
                    if(contatore == 0):
                        valMax = valore
                        valMin = valore 
                
                    if(valore=="N/D"): # Controllo che il valore non sia un numero
                        contatoreND += 1
                    else:
                        sommaValori += valore
                        contatore += 1

                        # Ricerca val max/min e mesi max/min
                        if(valMax <= valore):
                            valMax = valore
                        if(valMin >= valore):
                            valMin = valore

    for città, *dati in dati_Pluviometrici:
        for mese, valore in i:
            # Ricerca val max/min e mesi max/min
            if(valMax == valore):
                listaMesiMax.append(mese)
            if(valMin == valore):
                listaMesiMin.append(mese)

    
    media = sommaValori / contatore

    if(contatore > 0):
        return (media, (valMax, listaMesiMax), (valMin, listaMesiMin)) 
    if(contatoreND == 12):
        return ("N/D")           

nome = input("Inserisci il nome della città che di cui vuoi visualizzare i dati:")
print(f"(media, (valMax, listaMesiMax), (valMin, listaMesiMin)) : {datiTuaCittà(nome)}")