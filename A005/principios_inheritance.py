import datetime
import math

class LivingBeing:
    def __init__(self, name: str, birth_date: datetime.date):
        self.name = name
        self.birth_date = birth_date

    @property
    def age(self) -> int:
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)

    def __str__(self) -> str:
        return 'Name: '+ self.name + ', Birth Date: ' + self.birth_date.strftime('%Y/%m/%d')

    def make_a_sound(self, sound: str):
        print(f'{self.name} makes a sound: "{sound}"')

class Person(LivingBeing):
    def __init__(self, name: str, last_name: str, birth_date: datetime.date):
        super().__init__(name, birth_date)
        self.last_name = last_name

    def talk(self, words: str):
        return self.make_a_sound(words)

    def __str__(self) -> str:
        return 'Full Name: '+ self.name + ' ' + self.last_name + ', Birth Date: ' + self.birth_date.strftime('%Y/%m/%d')

class Dog(LivingBeing):
    def __init__(self, name: str, birth_date: datetime.date, breed: str):
        super().__init__(name, birth_date)
        self.breed = breed

    def bark(self):
        return self.make_a_sound('Woof! Woof!')

    def __str__(self) -> str:
        return 'Name: '+ self.name + ', Breed: ' + self.breed + ', Birth Date: ' + self.birth_date.strftime('%Y/%m/%d')

class Resume:
    def __init__(self, person: Person, experience: list[str]):
        self.person = person
        self.experience = experience

    @property
    def total_experiences(self) -> int:
        return len(self.experience)

    @property
    def current_company(self) -> str:
        return self.experience[-1]

    def add_experience(self, new_experience: str):
        self.experience.append(new_experience)
    
    def __str__(self) -> str:
        return f"{self.person.name} {self.person.last_name} is {self.person.age} years old and has worked on {self.total_experiences} companies. Currently works for {self.current_company}."


joao = Person('João', 'Silva', datetime.date(2000, 12, 31))
resume_joao = Resume(joao, ['Bar do Zé', 'Bar do Jão', 'Bar Samambaia'])

print(resume_joao.person, resume_joao.person.age)
print(resume_joao)
resume_joao.add_experience('Mercearia do Chico')
print(resume_joao)

rex = Dog('Rex', datetime.date(2020, 1, 1), 'Vira-Lata')
print(rex)
print(rex.age)
rex.bark()
joao.talk(f"Hi, {rex.name}!")