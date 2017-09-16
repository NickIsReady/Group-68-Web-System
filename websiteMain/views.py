from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
# Create your views here.

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