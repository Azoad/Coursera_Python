"""clas again"""


class PartyAnimal:  # pylint: disable=R0903
    """docstring"""
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(nam, "constructed")

    def party(self):
        """docstring for party metod"""
        self.x = self.x + 1
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal):
    """FootballFan is a class that extends PartyAnimal"""
    points = 0

    def touchdown(self):
        """docstring"""
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('jim')
j.party()
j.touchdown()
