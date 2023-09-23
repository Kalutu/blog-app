from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "articles"

urlpatterns = [
    path('', article_list, name='list'),
    path('create/', article_create, name='create'),
    path('<slug>/', article_detail, name='detail'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)