from django.db import models

# Create your models here.
class Person(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    img=models.ImageField(null=True,blank=True)
    email=models.EmailField()
    startdate=models.DateField()
    enddate=models.DateField(null=True,blank=True)
    salary=models.FloatField(default=0.0)
    isActive=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)