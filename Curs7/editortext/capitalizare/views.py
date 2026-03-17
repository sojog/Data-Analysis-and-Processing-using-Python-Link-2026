from django.shortcuts import render

# Create your views here.

def text_view(request, text:str):
	capitalized_text = text.capitalize()
	context = {
		"text" : capitalized_text
	}
	return render(request, 'text.html', context)

def cuvant_view(request):
	context = {}
	if request.GET.get('word'):
		capitalized_text = request.GET.get('word').capitalize()
		context["word"] = capitalized_text.capitalize()
	return render(request, 'cuvant.html', context)
