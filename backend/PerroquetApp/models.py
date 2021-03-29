from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "To reset your password, go to: https://perroquet.srvz-webapp.he-arc.ch/reset-password/{}".format(reset_password_token.key)

    send_mail(
        # title:
        "Perroquet password reset",
        # message:
        email_plaintext_message,
        # from:
        "jonatan.baumgartner@he-arc.ch",
        # to:
        [reset_password_token.user.email]
    )


class Message(models.Model):
    """Table schema to store articles."""
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="author")
    content = models.TextField()
    replyTo = models.ForeignKey("PerroquetApp.Message", null=True,on_delete=models.SET_NULL, related_name="replyToMessage")

    def __str__(self):
        return '%s' % self.content

class Like(models.Model):
    """Table schema to store articles."""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey("PerroquetApp.Message", on_delete=models.CASCADE, related_name="message")

    def __str__(self):
        return "like"

class Profile(models.Model):
    """Table schema to store profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.CharField(max_length=255)
    location = models.CharField(max_length=30, blank=True)
    birthDate = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Follow(models.Model):
    """Table schema to store follow."""
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    date_follow = models.DateTimeField()

    def __str__(self):
        return '%s' % self.name