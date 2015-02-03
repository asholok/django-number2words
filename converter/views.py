from django.shortcuts import render
from models import Engine

def index(request):
	return render(request, 'converter/index.html', {'engine': Engine()})

def results(request):
	language = request.POST['language']
	currency = request.POST['currency']
	number = request.POST['number'].strip()

	return render(request, 'converter/index.html', {'engine': Engine(language, currency, number)})

print Engine.info
# Create your views here.
