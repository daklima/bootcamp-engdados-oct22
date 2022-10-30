import datetime
import math

class Person:
    def __init__(self, name: str, last_name: str, birth_date:datetime.date):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self) -> str:
        return 'Full Name: '+ self.name + ' ' + self.last_name + ', Birth Date: ' + self.birth_date.strftime('%Y/%m/%d')
    
    @property
    def age(self) -> int:
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)

joao = Person('João', 'Silva', datetime.date(2000, 12, 31))

print(joao)
print(joao.name, joao.last_name, joao.birth_date)
print(joao.age)