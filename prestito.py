# File per classe prestito e i suoi metodi
class Prestito:
    def __init__(self, codice, data, strumento, cognome_allievo):
        self.__codice = codice
        self.__data = data
        self.__strumento = strumento  # oggetto strumento per cui si ha il prestito
        self.__cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.__codice}{self.__data}{self.__strumento}{self.__cognome_allievo}"

    # metodi getter
    @property
    def codice(self):
        return self.__codice
    @property
    def data(self):
        return self.__data
    @property
    def strumento(self):
        return self.__strumento
    @property
    def cognome_allievo(self):
        return self.__cognome_allievo


