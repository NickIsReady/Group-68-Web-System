from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
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

	return render(request, 'websiteMain/index.html')

	#return render(request, 'websiteMain/index.html')
	#return HttpResponse('<p>Hello World</p>')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponse("You're logged in")
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
	
def contacts(request):
	return render(request, 'websiteMain/contacts.html')
	
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

class UserFormView(View):
	form_class = UserForm
	template_name = ''
	
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
	
	def post(self, request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			
			user = form.save(commit=False)
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password=password)
			
			if user is not None:
				login(request, user)
				return redirect('information')
			
		return render(request, self.template_name, {'form': form})	
			
			
			
			

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

