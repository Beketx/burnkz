from django.urls import path
from .views import Test

urlpatterns = [
    path('api/', Test),
]