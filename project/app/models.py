from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

class registration(models.Model):
    name = models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    contactnumber=models.IntegerField()
class fileupload(models.Model):
    name=models.CharField(max_length=20)
    file=models.FileField()


