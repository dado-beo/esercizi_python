"""
**ESERCIZIO 1 : PAGELLE**

Crea una classe che rappresenti una **pagella scolastica**. La classe accetta in input una lista di numeri (voti) che rappresentano le valutazioni in ciascuna materia.

La classe deve avere queste funzionalità:

1. Stampando un oggetto `Pagella` il risultato sarà la lista dei voti *(implementare `__repr__`)*

2. La classe deve avere il metodo `media()`: ritorna la media aritmetica dei voti della pagella


3. La classe deve supportare l’**indexing**, ossia indicando l’indice si ottiene il voto corrispondente *(implementare `__getitem__`)*

   ```python
   p = Pagella([6, 8, 7])
   print(p[1])  # stampa 8
   ```

4. Confrontando due oggetti `Pagella`, il risultato sarà `True` se contengono esattamente gli stessi voti nello stesso ordine, `False` altrimenti *(implementare `__eq__`)*

5. Sottraendo una `Pagella` da un'altra si ottiene una nuova `Pagella` con la differenza tra i voti nelle stesse posizioni *(implementare `__sub__`)*


6. La classe deve avere il metodo `impegno()`: ritorna una misura dell’impegno complessivo calcolata come **radice quadrata del prodotto scolastico** della pagella con sé stessa
   *(es. `Pagella([6, 8])` → `√(6² + 8²) = √(100) = 10.0`)*

**Nota**: Per i punti 4, 5 le pagelle devono avere la **stessa dimensione**. In caso contrario, stampare il messaggio
> `"Le pagelle hanno un numero diverso di materie e non possono essere confrontate"`
> e restituire `None`.
---
"""
import math
class Pagella:
    def __init__(self):
        self.values = []

    def __repr__(self):
        return str(self.values) # il risultato sarà la lista dei voti

    def media(self): # ritorna la media aritmetica dei voti della pagella
        somma = 0
        n = 0
        for i in self.values:
            somma += i
            n += 1
        return round(somma / n, 2) # Media

    def __getitem__(self, indice): # indicando l’indice si ottiene il voto corrispondente
        return self.values[indice] 

    def __eq__(self, vector): # Confrontando due oggetti `Pagella`, il risultato sarà `True` se contengono esattamente gli stessi voti nello stesso ordine, `False` altrimenti
        if len(self.values) == len(vector.values): # controllo la lunghezza
            for a, b in zip(self.values, vector.values):
                if a != b:
                    return False
            return True # se non è stato fermato il codice ritorna true
        print("La dimensione delle due liste è differente!")
        return None
    
    def __sub__(self, vector): # Sottraendo una `Pagella` da un'altra si ottiene una nuova `Pagella` con la differenza tra i voti nelle stesse posizioni
        listaSottrazioni = []
        if len(self.values) == len(vector.values): # controllo la lunghezza
            for a, b in zip(self.values, vector.values):
                listaSottrazioni.append(a -b)
            return Pagella(listaSottrazioni) # se non è stato fermato il codice ritorna un nuovo oggetto Pagella
        print("La dimensione delle due liste è differente!")
        return None
    
    def impegno(self): # La classe deve avere il metodo `impegno()`: ritorna una misura dell’impegno complessivo calcolata come **radice quadrata del prodotto scolastico** della pagella con sé stessa
        somma = 0
        for i in self.values:
            somma += i * i
        return round(math.sqrt(somma), 2)

# Creazione oggetti pagella
p1 = Pagella([6, 8, 7])

media = p1.media()
print(f"La media: {media}")

indice = 1
print(f"Ecco il dato all'indice 1: {p1.__getitem__(indice)}")

veroOfalso = p1.__eq__([2, 8, 9])
if(veroOfalso == True):
    print("Contengono esattamente gli stessi voti nello stesso ordine")
else:
    print("Non contengono esattamente gli stessi voti nello stesso ordine")

sottrazione = p1.__sub__([[2, 8, 9]])
if(sottrazione != None):
    print(f"Ecco l'oggetto dato dalla sottrazione: {sottrazione} ")

radice = p1.impegno()
print(f"Ecco l'impegno complessivo: {radice}")

