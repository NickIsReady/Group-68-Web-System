from django.conf.urls import include, url
from . import views

urlpatterns = [
#Main Pages
    url(r'^$', views.index, name='index'),
	url(r'^/information', views.information, name='information'),
	url(r'^/help', views.help, name='help'),
	url(r'^/contacts', views.contacts, name='contacts'),
    url(r'^home', views.index, name='index'),
    
#Data Stores

    
]
