from stand import Stand

class Stanpreseelettriche(Stand):
    def __init__(self, codice, mq, padiglione, prezzo_base, prese_extra):
        super().__init__(codice, mq, padiglione, prezzo_base)
        self.prese_extra = int(prese_extra)

    def calcola_prezzo(self):
        # Sovrapprezzo del 7% per ogni presa extra
        return self.prezzo_base * (1 + 0.07 * self.prese_extra)

