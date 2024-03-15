from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    """Destination model"""
    title = models.CharField(max_length=255)
    days = models.IntegerField(default=1)
    place = models.CharField(max_length=255)
    bathroom = models.IntegerField(default=1)
    bedroom = models.IntegerField(default=1)
    price = models.IntegerField()
    img = models.ImageField(upload_to='destination/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Joy'
        verbose_name_plural = 'Joylar'

class Social(models.Model):
    """Social model"""
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ijtimoiy tarmoq'
        verbose_name_plural = 'Ijtimoiy tarmoqlar'

class AboutUs(models.Model):
    """AboutUs model"""
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizdalar'



class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    


