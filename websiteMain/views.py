from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from email.policy import strict
from .models import *

#Main View Patterns

def index(request):
	return render(request, 'websiteMain/index.html')
	
def information(request):
	return render(request, 'websiteMain/information.html')

def help(request):
	return render(request, 'websiteMain/help.html')
	
def contacts(request):
	return render(request, 'websiteMain/contacts.html')

def home(request):
	return render(request, 'websiteMain/index.html')


#Data View Patterns

#Shows all the malls stored in the DB
def malls(request):
	all_malls = Mall.objects.all()
	html = ''
	for mall in all_malls:
		url = '/malls/' + str(mall.mall_ID) + '/'
		html += '<a href="' + url + '">' + mall.name + '</a><br>'
	return HttpResponse("Details for malls in DB<br/>" + html + "<br/>End of information")

#Shows a mall using its mall_ID
def mall_detail(request, mall_ID):
	return HttpResponse("<h2>Details for Mall ID: " + str(mall_ID) 
					+ "</h2>")