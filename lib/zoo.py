from lib.animal import Animal

class Zoo:
    all=[]

    def __init__(self, name, location):
        self.name=name
        self.location=location
        Zoo.all.append(self)
    
    @property
    def animals(self):
        return[a for a in Animal.all if a.zoo_instance == self]

    @property
    def animal_species(self):
        return list({a.species for a in Animal.all if a.zoo_instance == self})

    
    def find_by_species(self, species_finder):
        return [a.nickname for a in self.animals if a.species == species_finder]

    
    @property
    def animal_nicknames(self):
        return [a.nickname for a in self.animals]

    @classmethod
    def find_by_location(cls, given_location):
        return [z.name for z in cls.all if z.location == given_location]
    

    



