from django import forms
from  .models import Orders
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Dateinput(forms.DateInput):
    input_type= 'date'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        widgets = {
            'order_date':Dateinput(),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2','first_name','last_name')
