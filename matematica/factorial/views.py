from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from functools import reduce


def calculeaza_factorial(n):
    produs = 1
    for i in range(1, n + 1):
        produs *= i
    return produs

def calculeaza_factorial_V2(n):
    if n == 0 or n == 1:
        return 1
    return n * calculeaza_factorial_V2(n - 1)




def factorial_view(request, n):
    try:
        n = int(n)
        
    except:
        return HttpResponse("Factorialul trebuie sa fie numar... !")
    
    if n < 0 :
        return HttpResponse("Factorialul trebuie sa fie >= 0..")

    
   
        
    produs = reduce(lambda x, y : x * y, range(1, n))
    return HttpResponse(f"{n}! = {produs} ")

    



