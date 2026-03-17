from django.shortcuts import render

# Create your views here.

def text_view(request, text:str):
	capitalized_text = text.capitalize()
	context = {
		"text" : capitalized_text
	}
	return render(request, 'text.html', context)
