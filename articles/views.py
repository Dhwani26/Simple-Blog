from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def article_list(request):
    a = Article.objects.all().order_by('date') # send this data to the article_list template
    return render(request , 'articles/article_list.html' , {'articles' : a}) # we have passed data as dictionary

def article_detail(request , slug):
    a = Article.objects.get(slug = slug)
    return render(request, 'articles/article_detail.html' , {'article' : a})

@login_required(login_url = '/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if(form.is_valid()):
            #save to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form' : form})