from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, mq, padiglione, prezzo_base, posizione):
        super().__init__(codice, mq, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        # Sovrapprezzo fisso del 30%
        return self.prezzo_base * 1.30
