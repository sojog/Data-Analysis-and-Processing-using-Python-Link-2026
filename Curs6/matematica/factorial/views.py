from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def factorial_view(request, n):

    if n >= 0:
        factorial_n = 1
        for i in range(1, n + 1):
            factorial_n = i * factorial_n
    else:
        factorial_n = "Imposibil"

    return HttpResponse(factorial_n)