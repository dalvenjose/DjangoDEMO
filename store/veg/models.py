from django.db import models

# Create your models here.

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name =models.CharField(max_length=200 ,null=False ,blank=False)
    customer_number=models.IntegerField(max_length=10 ,null=False, blank=False, unique=True)
    customer_address=models.TextField(max_length=400)
    order_date = models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.customer_name
    
class fruits(models.Model):
    fruit_id=models.AutoField(primary_key=True)
    fruit_name=models.CharField(max_length=200 ,null=False ,blank=False)

    fruit_price=models.IntegerField(max_length=10 ,null=False, blank=False)
    fruit_image=models.ImageField(upload_to='fruits')
    def  __str__(self):
        return self.fruit_name

class student(models.Model):
    rollno=models.IntegerField(primary_key=True , unique=True)
    name = models.CharField(max_length=200 ,null=False ,blank=False)
    age=models.IntegerField(max_length=10 ,null=False, blank=False)
    marks=models.IntegerField(max_length=10 ,null=False, blank=False)
    def  __str__(self):
        return self.name