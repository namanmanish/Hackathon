from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
	if request.method == 'POST': 
	    form = Imageform(request.POST, request.FILES) 

	    if form.is_valid(): 
	        form.save() 
	        messages.success(request, "saved in folder media/images")
	        return redirect('/result') 
	else: 
	    form = Imageform() 
	return render(request, 'crop/form.html/', {'form' : form})

def result(request):
	return HttpResponse("<h1>hi</h1>")