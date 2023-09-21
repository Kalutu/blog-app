from django.urls import path
from .views import *

urlpatterns = [
    path('', article_list),
]
