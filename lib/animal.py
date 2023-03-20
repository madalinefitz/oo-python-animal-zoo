class Animal:
    all = []

    def __init__(self, species, weight, nickname, zoo_instance):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo_instance = zoo_instance
        Animal.all.append(self)

    @classmethod
    def find_by_species(cls, given_species):
        return[a.nickname for a in cls.all if a.species == given_species]
