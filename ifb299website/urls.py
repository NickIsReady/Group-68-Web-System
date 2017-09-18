"""ifb299website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from websiteMain import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#Main Pages
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
	url(r'^information$', views.information, name='information'),
	url(r'^help', views.help, name='help'),
	url(r'^contacts', views.contacts, name='contacts'),
	url(r'^register', views.register, name='register'),
	#url(r'^login', views.user_login, name ='login'),
	url(r'^logout', views.user_logout, name='logout'),
	url('^', include('django.contrib.auth.urls')),
  
#Data Pages
        # /information/malls
    url(r'^information/malls$', views.malls, name='malls'),
    
        # /information/malls/#/
    url(r'^mallGet/$', views.mall_detail, name='mallGet'),
        
        # /hotels
    url(r'^hotels', views.hotels, name='hotels'),
        # /hotels/#/
    url(r'^hotels/(?P<hotel_ID>[0-9]+)/$', views.hotel_detail, name='hotel_detail'),
    
        # /Parks
    url(r'^parks', views.parks, name='parks'),
        # /parks/#/
    url(r'^parks/(?P<park_ID>[0-9]+)/$', views.park_detail, name='park_detail'),
    
        # /College
    url(r'^colleges', views.colleges, name='colleges'),
        # /colleges/#/
    url(r'^colleges/(?P<college_ID>[0-9]+)/$', views.college_detail, name='college_detail'),
    
        # /Libraries
    url(r'^libraries', views.libraries, name='libraries'),
        # /Libraries/#/
    url(r'^libraries/(?P<library_ID>[0-9]+)/$', views.library_detail, name='library_detail'),
    
        # /Zoos
    url(r'^zoos', views.zoos, name='zoos'),
        # /Zoos/#/
    url(r'^zoos/(?P<zoo_ID>[0-9]+)/$', views.zoo_detail, name='zoo_detail'),
    
        # /Museums
    url(r'^museums', views.museums, name='museums'),
        # /Museums/#/
    url(r'^museums/(?P<museum_ID>[0-9]+)/$', views.museum_detail, name='museum_detail'),
    
        # /Industries
    url(r'^industries', views.industries, name='industries'),
        # /Industries/#/
    url(r'^industries/(?P<industry_ID>[0-9]+)/$', views.industry_detail, name='industry_detail'),
    
        # /Restaurants
    url(r'^restaurants', views.restaurants, name='restaurants'),
        # /Restaurants/#/
    url(r'^restaurants/(?P<restaurant_ID>[0-9]+)/$', views.restaurant_detail, name='restaurant_detail'),
    
        # /Cities
    url(r'^cities', views.cities, name='cities'),
        # /Cities/#/
    url(r'^cities/(?P<city_ID>[0-9]+)/$', views.city_detail, name='city_detail'),
    

]
