from django.db import models
from django.utils.timezone import now

# Create your models here.

class ProfilePic(models.Model):
     profilePic = models.FileField(upload_to="profilePic/",max_length=250,null=True)
     Time=models.DateTimeField(default=now)

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     Message= models.TextField()
     Time=models.DateTimeField(default=now)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email