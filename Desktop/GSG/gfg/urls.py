"""gfg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from xml.dom.minidom import Document
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include

from gfg import views
from django.conf import settings
from django.conf.urls.static import static


#from gfg import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/', views.about),
    path('Services/', views.Services),
    path('portfolio/', views.portfolio),
    path('team/', views.Team),
    path('contact/', views.contact),
    path('saveEnquiry/', views.saveEnquiry, name="saveEnquiry"),
    path('useform/', views.useform),
    # in path name is use when the action method isue in html tag
    
    path('submitform/', views.submitform, name="submitform"),
    path('marksheet', views.marksheet),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd),
    path('newsDetails/', views.newsDetails)

    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

