from django.shortcuts import render

# Create your views here.

def shop_view(request):
	context = {}
	return render(request, 'shop.html', context)
