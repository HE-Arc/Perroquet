from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
#     path('messages/', views.MessageList.as_view()),
#     path('users/', views.UserList.as_view()),
#     # path('subscriptions/<int:pk>/', views.SubscriptionDetail.as_view()),
# ]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet,basename="yo1")
router.register(r'messages', views.MessageViewSet,basename="yo2")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]