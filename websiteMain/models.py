# This file forms part of the Smart-City Project 
# IFB299 S2-2017 Group 68 
# Description: This file represents system entities and variables

from django.db import models
from unittest.util import _MAX_LENGTH

# User Entity 
class User(models.Model):
    email_address = models.CharField(max_length=500)
    name_first = models.CharField(max_length=250)
    name_last = models.CharField(max_length=250)
    user_type = models.CharField(max_length=250)

# Mall Entity
class Mall(models.Model):
    mall_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Hotel Entity 
class Hotel(models.Model):
    hotel_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Park Entity 
class Park(models.Model):
    park_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# College Entity 
class College(models.Model):
    college_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Library Entity 
class Library(models.Model):
    library_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Zoo Entity 
class Zoo(models.Model):
    zoo_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Museum Entity 
class Museum(models.Model):
    museum_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Industry Entity 
class Industry(models.Model):
    industry_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# Restaurant Entity 
class Restaurant(models.Model):
    restaurant_ID = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    
# City Entity 
class City(models.Model):
    city_ID = models.CharField(max_length=500)
    Name = models.CharField(max_length=500)
    Service = models.CharField(max_length=500)