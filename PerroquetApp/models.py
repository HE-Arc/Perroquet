from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
    """Table schema to store articles."""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return '%s' % self.content

class Profile(models.Model):
    """Table schema to store profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.name

class Follow(models.Model):
    """Table schema to store follow."""
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    date_follow = models.DateTimeField()

    def __str__(self):
        return '%s' % self.name