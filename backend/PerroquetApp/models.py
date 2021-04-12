from datetime import datetime

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    content = models.TextField()
    replyTo = models.ForeignKey("PerroquetApp.Message", blank=True,null=True,on_delete=models.SET_NULL, related_name="replyToMessage")
    image = models.ImageField(upload_to ='img/%Y/%m/%d/',blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s' % self.content

class Like(models.Model):
    """Table schema to store articles."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    message = models.ForeignKey("PerroquetApp.Message", on_delete=models.CASCADE, related_name="like")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user","message"),)

    def __str__(self):
        return User.objects.get(pk=self.user_id).username +" like "+ str(Message.objects.get(pk=self.message_id).id)

class Profile(models.Model):
    """Table schema to store profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to ='img/%Y/%m/%d/',blank=True,null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user","following"),)

    def __str__(self):
        return User.objects.get(pk=self.user_id).username +" follow "+User.objects.get(pk=self.following_id).username