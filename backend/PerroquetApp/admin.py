from django.contrib import admin

from .models import Message
from .models import User
from .models import Like
from .models import Profile
from .models import Follow

# Register your models here.
admin.site.register(Message)
# admin.site.register(User)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Follow)