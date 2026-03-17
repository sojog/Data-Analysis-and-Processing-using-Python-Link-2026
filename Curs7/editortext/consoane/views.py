from django.shortcuts import render

# Create your views here.

def consoane_view(request):
	print("Request=", request)
	print("Dictionar GET", request.GET)
	text:str = request.GET.get("text")
	print("Textul citit este:", text)

	nr_consoane = 0
	if text:
		for i in text:
			if i.isalpha() and i not in "aeiouăî":
				nr_consoane += 1
				

	context = {
		"text" : text,
		"consoane" : nr_consoane
	}
	return render(request, 'consoane.html', context)

def inserare_view(request):
	if request.GET.get("text"):
		return consoane_view(request)
	
	context = {}
	return render(request, 'inserare.html', context)
