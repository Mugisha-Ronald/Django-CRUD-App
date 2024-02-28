from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Soldier(models.Model):
    army_no = models.CharField(max_length=500)
    rank = models.CharField(max_length=500)
    full_names = models.CharField(max_length=500)
    dateOfBirth = models.DateField(null=True,blank=True)
    formal_educ = models.CharField(max_length=500)
    courses_attnd = models.CharField(max_length=500)
    appointment = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='soldiers')
    


    def __str__(self):
        return self.full_names




class Address(models.Model):
    district = models.CharField(max_length=500)
    county = models.CharField(max_length=500)
    sub_county = models.CharField(max_length=500)
    parish = models.CharField(max_length=500)
    vilage = models.CharField(max_length=500)
    soldier = models.ForeignKey(Soldier,null=True,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.district
    





