from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    picture = models.ImageField(upload_to='artist_images/')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/artists/{self.id}/'
    
class Music_Class(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    full_description = models.TextField(null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)  # اضافه کردن فیلد متن آهنگ
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    genres = TaggableManager()
    viewer = models.IntegerField(default=0, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        if len(self.title) > 25:
            return self.title[:25] + "..."
        else:
            return self.title
        
    def get_absolute_url(self):
        return f'/all/{self.id}/'

    

class Comment(models.Model):
    article = models.ForeignKey(Music_Class, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=3000)
    writer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.writer) + " " + str(self.id)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    