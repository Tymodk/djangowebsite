from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Richting, Leraar, Klas, Contact

import datetime

def index(request):
	
	currentTime = datetime.datetime.now().hour
	greeting =''
	if currentTime < 6:
		greeting = "Goedenacht"
	elif currentTime <12 : 
		greeting ="Goedemorgen"
	elif currentTime >12 : 
		greeting ="Goedemiddag"
	elif currentTime > 18 :
		greeting ="Goedenavond"
	
	if 'visited' in request.COOKIES:
		greeting += " en welkom terug!"
	
	
	try:
		context = {'greeting': greeting, 'lastvisited': request.session['lastvisited']}
	except: 
		request.session['lastvisited'] = ""
		context = {'greeting': greeting, 'lastvisited': request.session['lastvisited']}
	response = render(request, 'schoolproject/index.html', context)	
	if not 'visted' in request.COOKIES:	
		response.set_cookie('visited', 'true', max_age = 365 * 24 * 60 * 60) 
	request.session['lastvisited'] = "schoolproject:index"
	try:
		if request.session['allvisited']:
			request.session['allvisited'] += "- index "
	except:
		request.session['allvisited'] = "index "
		
	return response

	

def aanbod(request):
	
	
	richtingenArray = Richting.objects.all()
	try:
		context = {'richtingenArray': richtingenArray,  'lastvisited': request.session['lastvisited']}
	except: 
		request.session['lastvisited'] = ""
		context = {'richtingenArray': richtingenArray,  'lastvisited': request.session['lastvisited']}
	
	response = render(request, 'schoolproject/aanbod.html', context)

	request.session['lastvisited'] = "schoolproject:aanbod"
	try:
		if request.session['allvisited']:
			request.session['allvisited'] += "- aanbod "
	except:
		request.session['allvisited'] = "aanbod "
	
	return response

def wie(request):
	
	lerarenArray = Leraar.objects.all()

	for leraar in lerarenArray :		
		leraar.klas = leraar.klas_set.all()
	try:
		context = {'lerarenArray': lerarenArray, 'lastvisited': request.session['lastvisited']}
	except: 
		request.session['lastvisited'] = ""
		context = {'lerarenArray': lerarenArray, 'lastvisited': request.session['lastvisited']}
	

	response = render(request, 'schoolproject/wieiswie.html', context)

	request.session['lastvisited'] = "schoolproject:wie"
	try:
		if request.session['allvisited']:
			request.session['allvisited'] += "- wie is wie "
	except:
		request.session['allvisited'] = "wie is wie "
	return response

def contact(request):
	
	try:
		context = {'lastvisited': request.session['lastvisited']}
	except: 
		request.session['lastvisited'] = ""
		context = {'lastvisited': request.session['lastvisited']}
	
	response = render(request, 'schoolproject/contact.html', context)

	request.session['lastvisited'] = "schoolproject:contact"
	try:
		if request.session['allvisited']:
			request.session['allvisited'] += "- contact "
	except:
		request.session['allvisited'] = "contact "
	return response

def contactlogic(request):

	contact_entry = Contact()
	contact_entry.email = request.POST['email']
	contact_entry.adres = request.POST['adres']
	contact_entry.inhoud = request.POST['inhoud']
	contact_entry.telenummer = request.POST['telenummer']
	contact_entry.save()

	return redirect('schoolproject:contact')

# Create your views here.
