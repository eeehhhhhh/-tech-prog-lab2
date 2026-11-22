
from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def express(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def get_age_in_human_years(self):
        pass


class Animal(Pet):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def happy_birthday(self):
        self._age += 1


class Turtle(Animal):
    def express(self):
        print(r"""                _,.---.---.---.--.._ 
            _.-' `--.`---.`---'-. _,`--.._
           /`--._ .'.     `.     `,`-.`-._\
          ||   \  `.`---.__`__..-`. ,'`-._/
     _  ,`\ `-._\   \    `.    `_.-`-._,``-.
  ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.
 (_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \
  `---'    `._ `---._/__,----`           `-. `-\
            /_, ,  _..-'                    `-._\
            \_, \/ ._(
             \_, \/ ._\
              `._,\/ ._\
                `._// ./`-._
                  `-._-_-_.-'

       """)

    def get_age_in_human_years(self):
        if self.get_age() <= 0:
            return 0
        return 15 + (self.get_age() - 1) * 2


class Parrot(Animal):
    def express(self):
        print(self.get_name() + ': "Hello!"')
        print(r"""    _\|/_
   ( o o )
  /   >   \

 |         |
  \_______/
    |   |
    _   _
""")

    def get_age_in_human_years(self):
        return self.get_age() * 5


class Person:
    def __init__(self, name, pet=None):
        self._name = name
        self._pet = pet

    def set_pet(self, pet):
        self._pet = pet

    def get_pet_info(self):
        print("--------------------")

        if self._pet is None:
            print(self._name, "has no pet yet")
            print("--------------------")
            return

        print("Pet for", self._name, "is named",
              self._pet.get_name())

        print("Age:", self._pet.get_age(),
              "year(s), about",
              self._pet.get_age_in_human_years(),
              "human years")

        print("And it expresses itself like this:")
        self._pet.express()

        print("--------------------")


kesha = Parrot("Kesha", 2)
zavala = Turtle("Zavala", 4)

kesha.happy_birthday()

jack = Person("Jack", kesha)
john = Person("John")

jack.get_pet_info()
john.get_pet_info()

john.set_pet(zavala)
john.get_pet_info()



