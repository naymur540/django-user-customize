from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
     fullname = models.CharField(max_length=100)
     mobile_number=models.CharField(max_length=15)
     gender=models.CharField(max_length=20)
     age = models.PositiveIntegerField()
     date_of_birth=models.DateField()
     present_address=models.TextField()
     permanent_address = models.TextField()
     last_education_name =models.CharField(max_length=100)
     institute_name=models.CharField(max_length=100)
     passing_year =models.IntegerField()
     grade =models.CharField(max_length=50)
     profile_image=models.ImageField(upload_to='Media/image')
     
     


