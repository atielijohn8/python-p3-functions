#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name = "Naureen" ):
    print(f"Hello, {name}!")
greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    #print(num1  + num2)
    return num1 + num2
add(1, 2)

def halve(number):
    if type(number) not in (int, float):
        return None
    return number / 2