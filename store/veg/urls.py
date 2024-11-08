from django.urls import  path
from .views import *

urlpatterns = [
    
    path('home/',home,name='home'),
    path('veg/',veg,name='veg'),
    path('fruits/',fruit,name='fruits'),
    path('grocery/',grocery,name='grocery'),
    path('ordernow/',Order,name='order'),
    path('register/',register_view,name='register'),
    path('',login,name='login')
]