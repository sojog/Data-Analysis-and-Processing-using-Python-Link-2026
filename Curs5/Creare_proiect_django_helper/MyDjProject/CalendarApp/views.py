from django.shortcuts import render
import numpy as np

# Create your views here.

def leap_years_view(request, start_year, stop_year):
	years = np.arange(start_year, stop_year + 1)
	leap_years = years[ (years % 400 == 0) |((years % 4 == 0) & (years % 100 != 0)  ) ]
	context = {
		'leap_years' : leap_years
	}
	return render(request, 'lear_years.html', context)
