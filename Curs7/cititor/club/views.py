from django.shortcuts import render

# Create your views here.

def validare_cnp_view(request):
	context = {}


	age = request.GET.get("age")
	gender = request.GET.get("gender")

	if age and gender:
		try:
			age = int(age)
		except:
			context["result"] = "Varsta invalida"
		
		if age in range(18, 71) or (age in range(16, 18) and gender == "f"):
			context["result"] = "Persoana are acces"
		else:
			context["result"] = "Persoana NU are acces"
	
	return render(request, 'cnp.html', context)



def validare_cnp_view_post_view(request):
	context = {}
	print("Request.POST", request.POST)

	age = request.POST.get("age")
	gender = request.POST.get("gender")

	if age and gender:
		try:
			age = int(age)
		except:
			context["result"] = "Varsta invalida"
		
		if age in range(18, 71) or (age in range(16, 18) and gender == "f"):
			context["result"] = "Persoana are acces"
		else:
			context["result"] = "Persoana NU are acces"
	

	return render(request, 'cnppost.html', context)
