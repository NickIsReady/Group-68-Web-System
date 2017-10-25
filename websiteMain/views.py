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
from itertools import chain

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

@login_required	
def information(request):
	return render(request, 'websiteMain/information.html')

def help(request):
	return render(request, 'websiteMain/help.html')

def categories(request):
	q1 = Mall.objects.all()
	q2 = Hotel.objects.all()
	q3 = Park.objects.all()
	q4 = College.objects.all()
	q5 = Library.objects.all()
	q6 = Zoo.objects.all()
	q7 = Museum.objects.all()
	q8 = Industry.objects.all()
	q9 = Restaurant.objects.all()
	
	template = loader.get_template('websiteMain/results.html')
	query = request.GET.get("query")
	
	if query:
		#queryset_list = queryset_list.filter(name__icontains=query)
		q1 = q1.filter(name__icontains=query)
		q2 = q2.filter(name__icontains=query)
		q3 = q3.filter(name__icontains=query)
		q4 = q4.filter(name__icontains=query)
		q5 = q5.filter(name__icontains=query)
		q6 = q6.filter(name__icontains=query)
		q7 = q7.filter(name__icontains=query)
		q8 = q8.filter(name__icontains=query)
		q9 = q9.filter(name__icontains=query)
		
		queryset_list=list(chain(q1, q2, q3, q4, q5, q6, q7, q8, q9))
		context = {
		'results': queryset_list
	}
		return HttpResponse(template.render(context, request))
	else: 
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
@login_required
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
def mall_detail(request, mall_id):
	mall = Mall.objects.get(id=mall_id)
	template = loader.get_template('websiteMain/mallGet.html')
	context = {
		'mall': mall,
	}
	return HttpResponse(template.render(context, request))

	
#Shows all the hotels stored in the DB
def hotels(request):
	all_hotels = Hotel.objects.all()
	template = loader.get_template('websiteMain/information_hotels.html')
	context = {
		'all_hotels': all_hotels
	}
	return HttpResponse(template.render(context, request))

#Shows a hotel using its hotel_ID
def hotel_detail(request, hotel_id):
	hotel = Hotel.objects.get(id=hotel_id)
	template = loader.get_template('websiteMain/hotelGet.html')
	context = {
		'hotel': hotel,
	}
	return HttpResponse(template.render(context, request))

#Shows all the parks stored in the DB
def parks(request):
	all_parks = Park.objects.all()
	template = loader.get_template('websiteMain/information_parks.html')
	context = {
		'all_parks': all_parks
	}
	return HttpResponse(template.render(context, request))

#Shows a park using its park_ID
def park_detail(request, park_id):
	park = Park.objects.get(id=park_id)
	template = loader.get_template('websiteMain/parkGet.html')
	context = {
		'park': park,
	}
	return HttpResponse(template.render(context, request))

#Shows all the colleges stored in the DB
def colleges(request):
	all_colleges = College.objects.all()
	template = loader.get_template('websiteMain/information_colleges.html')
	context = {
		'all_colleges': all_colleges
	}
	return HttpResponse(template.render(context, request))

#Shows a college using its college_ID
def college_detail(request, college_id):
	college = College.objects.get(id=college_id)
	template = loader.get_template('websiteMain/collegeGet.html')
	context = {
		'college': college,
	}
	return HttpResponse(template.render(context, request))

#Shows all the libraries stored in the DB
def libraries(request):
	all_libraries = Library.objects.all()
	template = loader.get_template('websiteMain/information_libraries.html')
	context = {
		'all_libraries': all_libraries
	}
	return HttpResponse(template.render(context, request))

#Shows a library using its library_ID
def library_detail(request, library_id):
	library = Library.objects.get(id=library_id)
	template = loader.get_template('websiteMain/libraryGet.html')
	context = {
		'library': library,
	}
	return HttpResponse(template.render(context, request))

#Shows all the zoos stored in the DB
def zoos(request):
	all_zoos = Zoo.objects.all()
	template = loader.get_template('websiteMain/information_zoos.html')
	context = {
		'all_zoos': all_zoos
	}
	return HttpResponse(template.render(context, request))

#Shows a zoo using its zoo_ID
def zoo_detail(request, zoo_id):
	zoo = Zoo.objects.get(id=zoo_id)
	template = loader.get_template('websiteMain/zooGet.html')
	context = {
		'zoo': zoo,
	}
	return HttpResponse(template.render(context, request))

#Shows all the museums stored in the DB
def museums(request):
	all_museums = Museum.objects.all()
	template = loader.get_template('websiteMain/information_museums.html')
	context = {
		'all_museums': all_museums
	}
	return HttpResponse(template.render(context, request))

#Shows a museum using its museum_ID
def museum_detail(request, museum_id):
	museum = Museum.objects.get(id=museum_id)
	template = loader.get_template('websiteMain/museumGet.html')
	context = {
		'museum': museum,
	}
	return HttpResponse(template.render(context, request))

#Shows all the industries stored in the DB
def industries(request):
	all_industries = Industry.objects.all()
	template = loader.get_template('websiteMain/information_industries.html')
	context = {
		'all_industries': all_industries
	}
	return HttpResponse(template.render(context, request))

#Shows a industry using its industry_ID
def industry_detail(request, industry_id):
	industry = Industry.objects.get(id=industry_id)
	template = loader.get_template('websiteMain/industryGet.html')
	context = {
		'industry': industry,
	}
	return HttpResponse(template.render(context, request))

#Shows all the restaurants stored in the DB
def restaurants(request):
	all_restaurants = Restaurant.objects.all()
	template = loader.get_template('websiteMain/information_restaurants.html')
	context = {
		'all_restaurants': all_restaurants
	}
	return HttpResponse(template.render(context, request))

#Shows a restaurant using its restaurant_ID
def restaurant_detail(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	template = loader.get_template('websiteMain/industryGet.html')
	context = {
		'restaurant': restaurant,
	}
	return HttpResponse(template.render(context, request))

#Shows all the restaurants stored in the DB
def restaurants(request):
	all_restaurants = Restaurant.objects.all()
	template = loader.get_template('websiteMain/information_restaurants.html')
	context = {
		'all_restaurants': all_restaurants
	}
	return HttpResponse(template.render(context, request))

#Shows a restaurant using its restaurant_ID
def restaurant_detail(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	template = loader.get_template('websiteMain/restaurantGet.html')
	context = {
		'restaurant': restaurant,
	}
	return HttpResponse(template.render(context, request))