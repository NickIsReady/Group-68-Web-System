from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from email.policy import strict

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

def malls(request):
	return HttpResponse("<h2>Details for malls")

#Data View Patterns

def mall_detail(request, mall_ID):
	return HttpResponse("<h2>Details for Mall ID: " + str(mall_ID) 
					+ "</h2>")