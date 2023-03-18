from typing import Protocol

class Vehicle(Protocol):
    def color(self) -> str:
        ...
    
class MyCar:
    def color(self):
        return "red"

class Tricycle:
    def color(self):
        return "orange"
    def size(self):
        return 12

class Strange:
    def size(self):
        return 13

def print_object(vehicle:Vehicle):
    print(vehicle.color())

print_object(MyCar())
print_object(Tricycle())
print_object(Strange()) # here type checkers and linting will point out an error that Strange do not comform to the protocol
#the code will still run but ﻿print_object(Strange()) will cause an error duing runtime