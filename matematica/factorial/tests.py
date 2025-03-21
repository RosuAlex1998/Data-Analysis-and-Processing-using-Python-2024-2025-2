from django.test import TestCase

# Create your tests here.


## 8! = 8 * 7!
## 7! = 7 * 6!


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(7))

