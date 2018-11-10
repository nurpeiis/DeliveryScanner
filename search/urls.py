from django.urls import include,  path
from .views import *
from search import settings
app_name = 'search'
urlpatterns = [
    path('', IndexView.as_view(), name = 'home' ), 
    ]