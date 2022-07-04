from django.db import models

from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='memes')
    likes = GenericRelation(Like)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'