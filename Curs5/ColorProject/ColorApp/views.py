from django.shortcuts import render

import numpy as np

# Create your views here.

def random_color_view(request):
    r, g, b = np.random.randint(0, 255, 3)
    context = {"red":r, "green":g, "blue":b}
    return render(request, "random_color.html", context)

def hex_color_view(request, hexcolor):
    
    context = {"hexcolor" : hexcolor}
    return render(request, "hexcolor.html", context)