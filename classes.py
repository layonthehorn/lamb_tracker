from datetime import datetime
import sys

# tries to import colorama from ENV.
try:
    from dateutil import relativedelta
except ImportError:
    print("Failed to import date-util. Check if installed in ENV.")
    print("pip install python-dateutil")
    sys.exit(1)


class Sheep:
    """This will contain all the base data that every sheep should have."""
    def __init__(self, name, number, mother, father, dob, gender):
        self.__name = name
        self.__number = number
        self.__mother = mother
        self.__father = father
        self.__dob = []
        self.__gender = gender
        self.__immune = False
        for time in dob.split("/"):
            self.__dob.append(int(time))

    @property
    def date_of_birth(self):
        # mm/dd/yyy
        return f"{self.__dob[0]}/{self.__dob[1]}/{self.__dob[2]}"

    @property
    def mother(self):
        return self.__mother

    @property
    def father(self):
        return self.__father

    @property
    def gender(self):
        return self.__gender

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def immunity(self):
        return self.__immune

    @immunity.setter
    def immunity(self, new):
        if not isinstance(new, bool):
            raise ValueError(f"Cannot assign non-boolean value on {self.name}, {self.number}")
        elif new:
            self.__immune = new
        elif self.__immune and not new:
            raise ValueError(f"Cannot unmark immunizations on {self.name}, {self.number}")

    def get_age(self):
        current_date = datetime.now()
        # yyyy/mm/dd
        birth = datetime(self.__dob[2], self.__dob[0], self.__dob[1])
        age = relativedelta.relativedelta(current_date, birth)
        return f"{self.name}, {self.number}:"\
               f"\nIs {age.days} days, {age.months} months, {age.years} years old."

    # print('{} years {} months {} days'.format(years, months, days))


class Child(Sheep):
    """This contains the various data related to lambs.
    Immunizations, DOB, Age, Gender, size of birth, Mother, and Father."""
    def __init__(self, name, number, mother, father, dob, gender):
        Sheep.__init__(self, name, number, mother, father, dob, gender)


class Mother(Sheep):
    """This is to track mothers.
    Age, DOB, and Average birth number"""
    def __init__(self, name, number, mother, father, dob, gender):
        Sheep.__init__(self, name, number, mother, father, dob, gender)


class Father(Sheep):
    def __init__(self, name, number, mother, father, dob, gender):
        Sheep.__init__(self, name, number, mother, father, dob, gender)


if __name__ == "__main__":
    sheep_test = Child("roger", "12", "mary", "bob", "1/12/2020", "male")
    print(sheep_test.get_age())
