from django.db import models

# Create your models here.
class Message(models.Model):
    """Table schema to store articles."""
    author = models.ForeignKey('PerroquetApp.User', on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.content

class User(models.Model):
    """Table schema to store auhtors."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name