## Basic Functions 

## Addition
def add(a, b):
    return a + b

## Subtraction
def sub(a, b):
    return a - b

## Multiplication
def mul(a, b):
    return a * b

## Division
def div(a, b):
    if b == 0:
        raise ValueError('Bad Input: b cannot be 0')
    return a / b