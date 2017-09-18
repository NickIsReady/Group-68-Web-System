from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
# Create your views here.
from email.policy import strict
from .models import *

#Main View Patterns


def index(request):

	#return render(request, 'websiteMain/index.html')

	#return render(request, 'websiteMain/index.html')
	#return HttpResponse('<p>Hello World</p>')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/information')
			else:
				return HttpResponse("Your account is disabled")
		else:
			#print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied")

	
	return render(request, 'websiteMain/index.html')

#login_required	
def information(request):
	return render(request, 'websiteMain/information.html')

def help(request):
	return render(request, 'websiteMain/help.html')

def categories(request):
	context = ['College','Library','Industry',
	'Hotel','Park','Zoo','Museum','Restaurant','Mall']
	return render(request, 'websiteMain/categories.html', {'categories': context})
	
def contacts(request):
	#[image of person, name, email]
	context = [['https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nicolas_Cage_2011_CC.jpg/220px-Nicolas_Cage_2011_CC.jpg','Patrick ​Breen',''],
			['https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nicolas_Cage_2011_CC.jpg/220px-Nicolas_Cage_2011_CC.jpg','Douglas ​Brennan',''],
			['https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nicolas_Cage_2011_CC.jpg/220px-Nicolas_Cage_2011_CC.jpg','Nicholas ​Constantine','nickconstantine3@gmail.com'],
			['https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nicolas_Cage_2011_CC.jpg/220px-Nicolas_Cage_2011_CC.jpg','Joshua ​Stephens',''],
			['https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Nicolas_Cage_2011_CC.jpg/220px-Nicolas_Cage_2011_CC.jpg','Tuan ​Luong','']]
	return render(request, 'websiteMain/contacts.html', {'names': context})

	
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save(commit=False)

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        #else:
         #   print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        

    # Render the template depending on the context.
    return render(request,
            'websiteMain/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/information')
			else:
				return HttpResponse("Your account is disabled")
		else:
			#print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'websiteMain/login.html')
		
# Use the login_required() decorator to ensure only those logged in can access the view.
#login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

#Create, Update, Delete items

class MallCreate(CreateView):
	model = Mall
	template_name = 'websiteMain/mall_form.html'
	fields = ['name','address','phone_number','city','email','image_url']

class MallUpdate(UpdateView):
	model = Mall
	template_name = 'websiteMain/mall_form.html'
	fields = ['name','address','phone_number','city','email','image_url']

class MallDelete(DeleteView):
	model = Mall
	success_url = reverse_lazy('websiteMain/index')


#Data View Patterns

#Shows all the malls stored in the DB
def malls(request):
	all_malls = Mall.objects.all()
	template = loader.get_template('websiteMain/information_malls.html')
	context = {
		'all_malls': all_malls
	}
	return HttpResponse(template.render(context, request))

#Shows a mall using its mall_ID
def mall_detail(request, mall_ID):
	template = loader.get_template('websiteMain/mallGet.html')
	context = {
		'mall_ID': mall_ID,
	}
	return HttpResponse(template.render(context, request))

	
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

#Shows all the Parks stored in the DB
def parks(request):
	all_parks = Park.objects.all()
	html = ''
	for park in all_parks:
		url = '/parks/' + str(park.park_ID) + '/'
		html += '<a href="' + url + '">' + park.name + '</a><br>'
	return HttpResponse("Details for parks in DB<br/>" + html + "<br/>End of information")

#Shows a park using its park_ID
def park_detail(request, park_ID):
	return HttpResponse("<h2>Details for Park ID: " + str(park_ID) 
					+ "</h2>")
	
#Shows all the Colleges stored in the DB
def colleges(request):
	all_colleges = College.objects.all()
	html = ''
	for college in all_colleges:
		url = '/college/' + str(college.college_ID) + '/'
		html += '<a href="' + url + '">' + college.name + '</a><br>'
	return HttpResponse("Details for colleges in DB<br/>" + html + "<br/>End of information")

#Shows a college using its college_ID
def college_detail(request, college_ID):
	return HttpResponse("<h2>Details for College ID: " + str(college_ID) 
					+ "</h2>")
	
#Shows all the Libraries stored in the DB
def libraries(request):
	all_libraries = Library.objects.all()
	html = ''
	for library in all_libraries:
		url = '/library/' + str(library.library_ID) + '/'
		html += '<a href="' + url + '">' + library.name + '</a><br>'
	return HttpResponse("Details for libraries in DB<br/>" + html + "<br/>End of information")

#Shows a library using its library_ID
def library_detail(request, library_ID):
	return HttpResponse("<h2>Details for Library ID: " + str(library_ID) 
					+ "</h2>")
	
#Shows all the Zoos stored in the DB
def zoos(request):
	all_zoos = Zoo.objects.all()
	html = ''
	for zoo in all_zoos:
		url = '/zoo/' + str(zoo.zoo_ID) + '/'
		html += '<a href="' + url + '">' + zoo.name + '</a><br>'
	return HttpResponse("Details for zoos in DB<br/>" + html + "<br/>End of information")

#Shows a zoo using its zoo_ID
def zoo_detail(request, zoo_ID):
	return HttpResponse("<h2>Details for Zoo ID: " + str(zoo_ID) 
					+ "</h2>")
	
#Shows all the Museums stored in the DB
def museums(request):
	all_museums = Museum.objects.all()
	html = ''
	for museum in all_museums:
		url = '/museum/' + str(museum.museum_ID) + '/'
		html += '<a href="' + url + '">' + museum.name + '</a><br>'
	return HttpResponse("Details for museums in DB<br/>" + html + "<br/>End of information")

#Shows a museum using its museum_ID
def museum_detail(request, museum_ID):
	return HttpResponse("<h2>Details for Museum ID: " + str(museum_ID) 
					+ "</h2>")
	
#Shows all the Industries stored in the DB
def industries(request):
	all_industries = Industry.objects.all()
	html = ''
	for industry in all_industries:
		url = '/industry/' + str(industry.industry_ID) + '/'
		html += '<a href="' + url + '">' + industry.name + '</a><br>'
	return HttpResponse("Details for industries in DB<br/>" + html + "<br/>End of information")

#Shows a industry using its industry_ID
def industry_detail(request, industry_ID):
	return HttpResponse("<h2>Details for Industry ID: " + str(industry_ID) 
					+ "</h2>")

#Shows all the Restaurants stored in the DB
def restaurants(request):
	all_restaurants = Restaurant.objects.all()
	html = ''
	for restaurant in all_restaurants:
		url = '/restaurant/' + str(restaurant.restaurant_ID) + '/'
		html += '<a href="' + url + '">' + restaurant.name + '</a><br>'
	return HttpResponse("Details for restaurants in DB<br/>" + html + "<br/>End of information")

#Shows a restaurant using its restaurant_ID
def restaurant_detail(request, restaurant_ID):
	return HttpResponse("<h2>Details for Restaurant ID: " + str(restaurant_ID) 
					+ "</h2>")
	
#Shows all the Cities stored in the DB
def cities(request):
	all_cities = City.objects.all()
	html = ''
	for city in all_cities:
		url = '/city/' + str(city.city_ID) + '/'
		html += '<a href="' + url + '">' + city.name + '</a><br>'
	return HttpResponse("Details for cities in DB<br/>" + html + "<br/>End of information")

#Shows a city using its city_ID
def city_detail(request, city_ID):
	return HttpResponse("<h2>Details for City ID: " + str(city_ID) 
					+ "</h2>")
	

