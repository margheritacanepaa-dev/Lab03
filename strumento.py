# File per classe strumento e i suoi metodi
class Strumento:
    def __init__(self, codice, nome, marca, anno, prezzo):
        self.__codice = codice
        self.__nome = nome
        self.__marca = marca
        self.__anno = int(anno)
        self.__prezzo = float(prezzo)

    def __str__(self):
        return f"{self.__codice} {self.__nome} {self.__marca} {self.__anno} {self.__prezzo}"

    # metodi getter
    @property
    def marca(self):
        return self.__marca
    @property
    def codice(self):
        return self.__codice
    @property
    def nome(self):
        return self.__nome
    @property
    def anno(self):
        return self.__anno
    @property
    def prezzo(self):
        return self.__prezzo