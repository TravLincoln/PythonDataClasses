# Data Class = A special kind of class that's designed mostly for holding data
#              without writing a lot of the boilerplate code for regular classes
#              Automatically generate: __init__, __repr__, __eq__
#              (Python 3.7)

from dataclasses import dataclass, field

# must add decorator @dataclass to declare a data class
# (frozen=True) makes any object created from the data class immutable
@dataclass (frozen=True)
class Person:

    # method __init__ is provided. We just need to provide data types
    name: str
    age: int

    # field used to customize how individual attributes behave
    # password field will be hidden when objects are created
    password: str = field(repr=False)
    is_alive: bool = True

    # within a data class, the data class can automatically
    # call the  __post__init__() method
    # adds verification when trying to assign attributes
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person1 = Person("Spongebob", 30, "pineapple1")
person2 = Person("Patrick", 35, "password")


print(person1)
print(person2)
