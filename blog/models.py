from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField
# from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=20,default=None)
    # slug=models.CharField(max_length=130)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    timeStamp=models.DateTimeField(default=now)
    content=models.TextField()
    # content=HTMLField()

    def __str__(self):
        return self.title + " by " + self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
