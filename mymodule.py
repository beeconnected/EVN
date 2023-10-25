class customer(object):
    def __init__(self, nummer, dauer, tarif):
        self.nummer = nummer
        self.dauer = dauer
        self.kosten = dauer*tarif

    def __eq__(self, other):
        if isinstance(other, customer):
            return self.nummer == other.nummer
        return False

    def addCosts (self, neuedauer, neuertarif) :
        self.kosten = self.kosten + (neuedauer*neuertarif)

