"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path , include
from . import views
from articles import views as article_views
from django.conf.urls.static import static
from django.conf import settings
# tell django to serve aur static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^articles/' , include('articles.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^$', article_views.article_list, name = 'home'),
    re_path(r'^about/$' , views.about)
]

urlpatterns += staticfiles_urlpatterns()
#this is a kind of a seting up phase 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

