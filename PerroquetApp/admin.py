from django.contrib import admin

from .models import Message
from .models import User
from .models import Like
from .models import Profile
from .models import Follow

# Register your models here.
admin.register(Message,admin.site)
# admin.register(User,admin.site)
admin.register(Like,admin.site)
admin.register(Profile,admin.site)
admin.register(Follow,admin.site)