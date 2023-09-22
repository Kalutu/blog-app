from django.urls import path
from .views import *


app_name = "articles"

urlpatterns = [
    path('', article_list, name='list'),
    path('<slug>/', article_detail, name='detail'),
]
