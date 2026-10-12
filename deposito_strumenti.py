# File per la classe DepositoStrumenti e i suoi metodi
import csv
from strumento import Strumento  #importo le alrte classi
from prestito import Prestito
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.__nome= nome
        self.__responsabile = responsabile
        self.__strumenti = []        # lista di tutti gli strumenti del deposito
        self.__prestiti=[]            # lista di tutti i prestiti del deposito

    # metodi getter e setter per il responsabile
    @property
    def responsabile(self):
        return self.responsabile
    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        self.__responsabile = nuovo_responsabile


    def __str__(self): # fz per stampare
        return f"{self.__nome}, {self.__responsabile}, {self.__strumenti}"


    # carica gli strumenti dal file csv
    def carica_file_strumenti(self, file_path):
        try:
            with open(file_path,"r") as infile:
                reader = csv.reader(infile)
                for row in reader:
                    cod=row[0].strip()     # estraggo i campi dalle righe
                    nome=row[1].strip()
                    marca=row[2].strip()
                    anno=int(row[3].strip())
                    prezzo=float(row[4].strip())
                    # creo nuovo oggetto "strumento" e aggiungo alla lista
                    nuovo_strumento= Strumento(cod, nome, marca, anno, prezzo)
                    self.__strumenti.append(nuovo_strumento)

        except FileNotFoundError:
            raise FileNotFoundError   # se non lo trova scatena eccezione


    # aggiunge gli strumenti al deposito
    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        codice_strum= f"S{len(self.__strumenti) + 1}"       # controllo il numero con len(), per non estrarre gli attributi privati
        nuovo_strumento = Strumento(codice_strum, tipo, marca, anno_acquisto,valore)
        self.__strumenti.append(nuovo_strumento)   # aggiungo l'oggetto strumento

        return nuovo_strumento


    # metodo per ordinare gli strumenti per marca
    def strumenti_ordinati_per_marca(self):
        return sorted(self.__strumenti, key=attrgetter('marca'))


    # metodo per creare un prestito
    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        strumento_trovato= None
        for strumento in self.__strumenti:           # controllo se lo strumento è nel deposito
            if strumento.codice == id_strumento:
                strumento_trovato = strumento
                break
        if strumento_trovato is None:
            raise Exception (f"Lo strumento non è nel sistema")

        # controllo se è gia in prestito
        for prestito in self.__prestiti:
            if prestito.strumento.codice == id_strumento:
                raise Exception(f"Lo strumento risulta già in prestito!")

        # se non è già in prestito, creo l'oggetto prestito e lo aggiungo
        numero_prestito = f"P{len(self.__prestiti) + 1}"
        prestito_effettuato = Prestito(numero_prestito,data, strumento_trovato, cognome_allievo)
        self.__prestiti.append(prestito_effettuato)

        return prestito_effettuato


    # metodo per terminare un prestito in corso
    def termina_prestito(self, id_prestito):
        prestito_trovato = None
        for prestito in self.__prestiti:        # controllo se c'è il prestito in corso
            if prestito.codice == id_prestito:
                prestito_trovato = prestito
                break
        if prestito_trovato is None:      # se non viene trovato
            raise Exception(f"Il codice del prestito non è nel sistema")

        self.__prestiti.remove(prestito_trovato)   # rimuovo dalla lista dei prestiti
        return prestito_trovato

