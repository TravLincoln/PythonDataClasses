# Data Class = A special kind of class that's designed mostly for holding data
#              without writing a lot of the boilerplate code for regular classes
#              Automatically generate: __init__, __repr__, __eq__
#              (Python 3.7)
from dataclasses import dataclass, field

# To make objects created from a data class immutable, use @dataclass (frozen=True)
@dataclass
class Person:
    name: str
    age: int
    # field used to customize how individual attributes behave
    # password attribute will not be visible when object is printed
    password: str = field(repr=False)
    is_alive: bool = True

    # After constructing the object
    # The data class can call a __post__ method

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be less than 0")

person1 = Person("Spongebob", 30, "pineapple1")
person2 = Person("Patrick", 35, "password")
person1.age = -1
print(person2)