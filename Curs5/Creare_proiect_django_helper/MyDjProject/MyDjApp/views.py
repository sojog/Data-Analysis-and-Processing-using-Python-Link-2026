from django.shortcuts import render

# Create your views here.

def food_view(request):
	context = {}
	return render(request, 'food.html', context)
