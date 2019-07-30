from django.urls import re_path
from . import views

#this is name spacing of urls
app_name = 'articles'

urlpatterns = [
    
    re_path(r'^$', views.article_list , name = 'list'),
    re_path(r'^create/$', views.article_create, name = 'create'),
    re_path(r'^(?P<slug>[\w-]+)$' , views.article_detail , name = 'detail'),
]
