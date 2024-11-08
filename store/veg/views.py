from django.shortcuts import render,redirect
from .models import *
from  .forms import *
from django.urls import reverse
from  django.contrib.auth.decorators import login_required



def login(request):
    return render(request, 'registration\login.html')
# Create your views here.
@login_required()
def home(request):
    return render(request, 'home.html')
def veg(request):
    return render(request, 'vegitables.html')
# def fruits(request):
#     return render(request, 'fruits.html')
def grocery(request):
    return render(request, 'grocery.html')


def Order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST) 
        if form.is_valid():
            form.save()
    form = OrderForm()
    dict_form= {
        'form' :form
    }
    return render(request ,'ordernow.html',dict_form)

def fruit(request):
    dict1 ={
        'dict1':fruits.objects.all()
    }
    return render(request, 'fruits.html', dict1)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    return render(request,'register.html',{'form':form})