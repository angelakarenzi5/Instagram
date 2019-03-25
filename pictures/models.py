from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='gram/', blank=True)
    bio= models.CharField(max_length =30)

def __str__(self):
        return self.user_name
        
def save_profile(self):
        self.save()

class Meta:
        ordering = ['user_name']

class likes(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'gram/', blank=True)
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =100)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(likes)
    comments = models.CharField(max_length =100)
    pub_date = models.DateTimeField(auto_now_add=True)

@classmethod
def todays_pictures(cls):
        today = dt.date.today()
        pictures = cls.objects.filter(pub_date__date = today)
        return pictures

@classmethod
def days_pictures(cls,date):
        pictures = cls.objects.filter(pub_date__date = date)
        return pictures

@classmethod
    
def search_by_title(cls,search_term):
        pictures = cls.objects.filter(title__icontains=search_term)
        return pictures

class PicturesRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
