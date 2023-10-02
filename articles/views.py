from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

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

def article_delete(request, pk):
   queryset = Article.objects.get(id=pk)
   if request.method == 'POST':
       queryset.delete()
       messages.success(request, 'Article deleted successfully')
       return redirect('articles:list')
   return render(request, 'articles/delete.html')

def article_edit(request, pk):
   queryset = Article.objects.get(id=pk)
   form = EditArticle(instance=queryset)
   if request.method == 'POST':
       form = EditArticle(request.POST, instance=queryset)
       if form.is_valid():        
            form.save()
            messages.success(request, 'Article updated successfully')
            return redirect('articles:list')
   return render(request, 'articles/edit_article.html', {"form": form})