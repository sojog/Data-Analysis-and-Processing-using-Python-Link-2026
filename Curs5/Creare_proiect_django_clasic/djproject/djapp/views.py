from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from djapp.models import Food

def fridge_view(request):
    return HttpResponse("elefant")



def computer_view(request):
    return HttpResponse("film")

def box_view(request):

    ## Iau toate modelele de tip FOOD
    food_list = Food.objects.all()
    context = {
        "food_objects" : food_list
    }
    return render(request, "variable.html", context)