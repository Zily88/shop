from django.test import TestCase

# Create your tests here.

def summa(a:int, b:int):
    print(a+b)

summa('b', 'a')

def umnozhenie(a, b) -> int:
    return a + b

print(umnozhenie('a', 'b'))
