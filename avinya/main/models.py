from django.db import models

# Create your models here.

class Team4(models.Model):
    no=models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
    rollno1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=100)
    rollno2 = models.CharField(max_length=20)
    name3 = models.CharField(max_length=100)
    rollno3 = models.CharField(max_length=20)
    name4 = models.CharField(max_length=100)
    rollno4 = models.CharField(max_length=20)
    
class Team5(models.Model):
    no=models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
    rollno1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=100)
    rollno2 = models.CharField(max_length=20)
    name3 = models.CharField(max_length=100)
    rollno3 = models.CharField(max_length=20)
    name4 = models.CharField(max_length=100)
    rollno4 = models.CharField(max_length=20)
    name5 = models.CharField(max_length=100)
    rollno5 = models.CharField(max_length=20)

class details(models.Model):
    no = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

