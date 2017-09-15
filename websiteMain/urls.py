from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^informationPage/', include('informationPage.urls')),
	url(r'^/information', views.information, name='information'),
	url(r'^/help', views.help, name='help'),
	url(r'^/contacts', views.contacts, name='contacts'),
]
