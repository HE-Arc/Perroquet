from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# urlpatterns = [
#     path('messages/', views.MessageList.as_view()),
#     path('users/', views.UserList.as_view()),
#     # path('subscriptions/<int:pk>/', views.SubscriptionDetail.as_view()),
# ]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet,'user')
router.register(r'messages', views.MessageViewSet,'message')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('PerroquetApp.auth.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', obtain_auth_token, name='api_token_auth'),
    # path('token/refresh/', obtain_auth_token, name='api_token_auth'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]