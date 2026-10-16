import csv
from stand import Stand
from standpreseelettriche import Stanpreseelettriche
from standpremium import StandPremium
from espositore import Espositore


class LingottoFiere:

    def __init__(self, nome="Lingotto Fiere"):
        """Inizializza gli attributi e le strutture dati"""

        self._nome = nome
        self.stands = {}
        self.espositori = {}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file ripulendo gli spazi"""
        try:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                for riga in reader:
                    if not riga:
                        continue


                    codice = riga[0].strip()

                    if codice.startswith("ES"):
                        codice_espositore = codice
                        nome = riga[1].strip()
                        cognome = riga[2].strip()
                        espositore = Espositore(codice_espositore, nome, cognome)
                        self.espositori[codice_espositore] = espositore

                    elif codice.startswith("ST"):
                        codice_stand = codice
                        superficie = riga[1].strip()
                        padiglione = riga[2].strip()
                        prezzo_base = riga[3].strip()

                        if len(riga) == 4:
                            stand = Stand(codice_stand, superficie, padiglione, prezzo_base)
                        elif len(riga) == 5:
                            campo_extra = riga[4].strip()
                            if campo_extra.isdigit():
                                stand = Stanpreseelettriche(codice_stand, superficie, padiglione, prezzo_base, campo_extra)
                            else:
                                stand = StandPremium(codice_stand, superficie, padiglione, prezzo_base, campo_extra)

                        self.stands[codice_stand] = stand

        except FileNotFoundError:
            raise FileNotFoundError(f"Il file {file_path} non è stato trovato.")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore ripulendo gli input"""

        codice_stand = codice_stand.strip()
        codice_espositore = codice_espositore.strip()

        if codice_stand not in self.stands:
            raise ValueError(f"Lo stand non esiste.")
        if codice_espositore not in self.espositori:
            raise ValueError(f"L'espositore non esiste.")

        stand = self.stands[codice_stand]
        espositore = self.espositori[codice_espositore]

        if not stand.disponibile:
            raise ValueError("Lo stand è già occupato.")
        if espositore.stand is not None:
            raise ValueError("L'espositore ha già uno stand.")

        stand.disponibile = False
        stand.espositore = codice_stand
        espositore.stand = codice_stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori"""
        for e in self.espositori.values():
            if e.stand is not None:
                print(f"{e.codice} {e.nome} {e.cognome} | Ha lo stand: {e.stand}")
            else:
                print(f"{e.codice} - {e.nome} {e.cognome} | Non ha alcuno stand")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        ordinati = sorted(self.stands.values(), key=lambda s: s.calcola_prezzo())

        risultato = []
        for s in ordinati:
            if s.disponibile:
                stato = "Disponibile"
            else:
                stato = "Occupato"
            testo = f"{s.codice_stand} | {s.superficie}mq | Padiglione {s.padiglione} | Prezzo: {s.calcola_prezzo():.2f}€ | {stato}"
            risultato.append(testo)

        return risultato


