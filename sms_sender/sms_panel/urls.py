from django.urls import path
from .views import tester
urlpatterns = [
    path('',tester , name = 'tester')
]
