class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"
    def __eq__(self, other):
        if self.nominator * other.denominator == self.denominator * other.nominator:
            return True
        else:
            return False

    def __add__(self, other):
        spodek = self.denominator * other. denominator
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        return Fraction(new_nominator, spodek)



