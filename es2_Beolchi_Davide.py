"""
**ESERCIZIO 2 : BIBLIOTECA E LIBRI**

Creare la classe `Biblioteca` per contenere una serie di oggetti `Libro`.

La classe `Biblioteca` deve contenere:

* un attributo che rappresenti una lista di libri presenti;
* un metodo per aggiungere un libro alla biblioteca;
* un metodo per rimuovere un libro (dato il codice ISBN);
* un metodo per visualizzare l’elenco dei libri disponibili;
* un metodo per cercare un libro dato il codice ISBN e restituire le sue informazioni.
"""

class Libro:
    def __init__(self, isbn, titolo, autore, anno): # Inizializza gli attributi del libro
          self.isbn = isbn
          self.titolo = titolo
          self.autore = autore
          self.anno = anno

    def __str__(self): # Restituisce una descrizione leggibile del libro
        return f'{self.titolo} di {self.autore} ({self.anno}) - ISBN: {self.isbn} \n'

class Biblioteca:
    def __init__(self): # Inizializza la lista dei libri
        self.listaLibri = []

    def aggiungi_libro(self, libro): # Aggiunge un libro alla lista
        self.listaLibri.append(libro)

    def rimuovi_libro(self, isbn): # Rimuove un libro in base all'ISBN
        # Ricerca libro in base all'ISBN
        for libro in self.listaLibri:
            if libro.isbn == isbn:
                print(f"Libro {libro.titolo} ({libro.anno}) rimosso con successo")
                self.listaLibri.remove(libro)
                return 

        print(f"Libro {libro.nome} ({libro.anno}) non è stato rimosso con successo")
        return 

    def elenco_libri(self): # Restituisce la lista dei libri nella biblioteca
        lista = 'Libri presenti in biblioteca: \n' 
        for libro in self.listaLibri:
            lista += f'{libro.titolo} di {libro.autore} ({libro.anno}) - ISBN: {libro.isbn} \n'
        return lista

    def cerca_libro(self, isbn): # Restituisce il libro trovato o None se non esiste
        # Ricerca libro in base all'ISBN 
        for libro in self.listaLibri:
            if libro.isbn == isbn:
                print(str(libro))
                return 
        print(f"Il libro cercato non esiste")
        return None

# Dichiarazione libri
libro1 = Libro("9781234567897", "Il nome della rosa", "Umberto Eco", "1980")
libro2 = Libro("9789876543210", "1984", "George Orwell", "1949")
libro3 = Libro("9780007117116", "Il Signore degli Anelli", "J.R.R. Tolkien", "1954")

biblioteca = Biblioteca() # creazione oggetto biblioteca

# Aggiunta libri in biblioteca
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

# Elenco libri come richiesto
lista = biblioteca.elenco_libri()
print(lista)

# Ricerca libro come richiesto
print("Ricerca del libro con ISBN 9789876543210:")
isbn = "9789876543210"
biblioteca.cerca_libro(isbn)
print("Oppure:") # esempio di libro non trovato
isbn = "1111111111111"
biblioteca.cerca_libro(isbn)

# Rimozione libro come richiesto
print("Rimozione del libro con ISBN 9781234567897:")
isbn = "9781234567897"
biblioteca.rimuovi_libro(isbn)

# Elenco libri come richiesto
print("")
print("Libri presenti dopo la rimozione:")
lista = biblioteca.elenco_libri()
print(lista)

"""
OUTPUT ATTESO

Libri presenti in biblioteca:
Il nome della rosa di Umberto Eco (1980) - ISBN: 9781234567897
1984 di George Orwell (1949) - ISBN: 9789876543210
Il Signore degli Anelli di J.R.R. Tolkien (1954) - ISBN: 9780007117116

Ricerca del libro con ISBN 9789876543210:
1984 di George Orwell (1949) - ISBN: 9789876543210
Oppure:
Il libro cercato non esiste

Rimozione del libro con ISBN 9781234567897:
Libro "Il nome della rosa di Umberto Eco (1980)" rimosso con successo.

Libri presenti dopo la rimozione:
1984 di George Orwell (1949) - ISBN: 9789876543210
Il Signore degli Anelli di J.R.R. Tolkien (1954) - ISBN: 9780007117116
"""