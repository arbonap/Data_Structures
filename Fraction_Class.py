class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        #cross multiply:
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __eq__(self, one, two)
        self.one = one
        self.two = two

        return