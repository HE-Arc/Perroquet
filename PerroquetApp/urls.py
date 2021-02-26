from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('login',LoginView)

urlpatterns = [
    path('', include(router.urls)),
]