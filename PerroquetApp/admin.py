from django.contrib import admin

from .models import Message
from .models import User

# Register your models here.
admin.register(Message,admin.site)
admin.register(User,admin.site)