from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField
# from tinymce.models import HTMLField

# Create your models here.

class addService(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=20)
    # slug=models.CharField(max_length=130)
    SlugField = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    timeStamp=models.DateTimeField(default=now)
    description=models.TextField()
    code=models.TextField()
    # content=HTMLField()

    def __str__(self):
        return self.title + " - " + self.description