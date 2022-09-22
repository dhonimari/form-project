from django.db import models

# Create your models here.


class Mari(models.Model):
    Name=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=20,default="")
    Aadhar=models.IntegerField(default="")
    Department=models.CharField(max_length=20,default="")

    