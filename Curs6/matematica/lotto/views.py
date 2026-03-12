from django.shortcuts import render

# Create your views here.
import random

from django.http import HttpResponse

def random_number_view(request):
    nr = random.randint(1, 49)
    return HttpResponse(f"<h1>{nr}</h1>")

def six_random_numbers_view(request):
    # numere = [12, 3, 4, 5, 15,6]
    numere = random.sample(range(1, 50), 6)

    context = {"numere": numere}

    return render(request, "extragere.html", context)