from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# from autoslug import AutoSlugField

# Create your models here.

class ProfilePic(models.Model):
     profilePic = models.FileField(
         upload_to="profilePic/", max_length=250, null=True)
     Time = models.DateTimeField(default=now)


class Contact(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     phone = models.CharField(max_length=13)
     email = models.CharField(max_length=100)
     Message = models.TextField()
     Time = models.DateTimeField(default=now)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


class Todo(models.Model):
    sno = models.AutoField(primary_key=True)
    todotitle = models.CharField(max_length=20,null=True)
    tododescription=models.TextField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    time= models.DateTimeField(default=now)

    def __str__(self):
        return self.todotitle[0:15] + "..." + "by" + " " + self.user.username


# class Post(models.Model):
#     sno=models.AutoField(primary_key=True)
#     title=models.CharField(max_length=255)
#     author=models.CharField(max_length=20,default=None)
#     # slug=models.CharField(max_length=130)
#     slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
#     timeStamp=models.DateTimeField(default=now)
#     content=models.TextField()
#     # content=HTMLField()

#     def __str__(self):
#         return self.title + " by " + self.author