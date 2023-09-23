from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {"articles":articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {"article":article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('articles:list')

    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {"form":form})