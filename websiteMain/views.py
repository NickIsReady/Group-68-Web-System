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
	
#Shows all the hotels stored in the DB
def hotels(request):
	all_hotels = Hotel.objects.all()
	html = ''
	for hotel in all_hotels:
		url = '/hotels/' + str(hotel.hotel_ID) + '/'
		html += '<a href="' + url + '">' + hotel.name + '</a><br>'
	return HttpResponse("Details for hotels in DB<br/>" + html + "<br/>End of information")

#Shows a hotel using its hotel_ID
def hotel_detail(request, hotel_ID):
	return HttpResponse("<h2>Details for Hotel ID: " + str(hotel_ID) 
					+ "</h2>")
	
	