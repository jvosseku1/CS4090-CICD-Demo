#!/bin/python
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("b cannot be 0\n nothing divisible by 0")
    return a / b

def percent(a, b):
    if a > b:
        raise ValueError("a cannot be greater than b")
    if (a < 0 or a > 100) or (b < 0 or b > 100):
        raise ValueError("a and b must be between 0 and 100")
    return (a / b) * 100

def sqroot(a):
    if a < 0:
        raise ValueError("The radicand cannot be negative")
    return math.sqrt(a)

def sine(a):
    if a < 0 or a > 1:
        raise ValueError("a must be between 0 and 1")
    return math.sin(a)

def cosine(a):
    if a < 0 or a > 1:
        raise ValueError("a must be between 0 and 1")
    return math.cos(a)

def squared(a):
    return a ** 2

def logarithm(a, b):
    if b <= 1:
        raise ValueError("b must be greater than 1")
    if a < 1:
        raise ValueError("a must be greater than 0")
    return math.log(a, b)
