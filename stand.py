class Stand:
    def __init__(self, codice_stand,superficie, padiglione, prezzo_base):
        self.codice_stand = codice_stand
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = float(prezzo_base)
        self.disponibile = True

        self.espositore = None

    def calcola_prezzo(self):
        return self.prezzo_base