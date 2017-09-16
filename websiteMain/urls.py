from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^/information', views.information, name='information'),
	url(r'^/help', views.help, name='help'),
	url(r'^/contacts', views.contacts, name='contacts'),
	url(r'^/register', views.register, name='register'),
	url(r'^login', views.user_login, name ='login'),
	url(r'^logout', views.user_logout, name='logout'),
]
