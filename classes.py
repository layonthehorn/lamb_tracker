

class Sheep:
    """This will contain all the base data that every sheep should have."""
    def __init__(self, mother, father, dob):
        self.__mother = mother
        self.__father = father
        self.__dob = dob

    @property
    def date_of_birth(self):
        return self.__dob

    @property
    def mother(self):
        return self.__mother

    @property
    def father(self):
        return self.__father


class Child(Sheep):
    """This contains the various data related to lambs.
    Immunizations, DOB, Age, Gender, size of birth, Mother, and Father."""
    def __init__(self, mother, father, dob):
        Sheep.__init__(self, mother, father, dob)


class Mother(Sheep):
    """This is to track mothers.
    Age, DOB, and Average birth number"""
    def __init__(self, mother, father, dob):
        Sheep.__init__(self, mother, father, dob)


class Father(Sheep):
    def __init__(self, mother, father, dob):
        Sheep.__init__(self, mother, father, dob)
