# pet_utils.py

class Pet:
    def __init__(self):
        self.name = None
        self.animal_type = None
        self.age = None

    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age


def create_pet(name, animal_type, age):
    pet_obj = Pet()
    pet_obj.set_name(name)
    pet_obj.set_animal_type(animal_type)
    pet_obj.set_age(age)
    return pet_obj

def get_pet_details(pet_obj):
    pet_details = {
        "name": pet_obj.get_name(),
        "animal_type": pet_obj.get_animal_type(),
        "age": pet_obj.get_age()
    }
    return pet_details

