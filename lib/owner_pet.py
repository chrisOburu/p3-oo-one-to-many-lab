class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name, pet_type, owner=""):
        self.name = name
        self.owner = owner
        self.pet_type = self.validate_pet(pet_type)
        Pet.all.append(self)
    
    @classmethod
    def validate_pet(cls,pet_type):
        if pet_type in cls.PET_TYPES:
            return pet_type
        else:
            raise ValueError("Invalid pet type")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)

    