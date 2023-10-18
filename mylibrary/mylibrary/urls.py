"""
URL configuration for mylibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from library import views

urlpatterns = [
    path('', views.show_start_page),
    path('showbooks/', views.show_showbooks_page),
    path('addbook/', views.show_addbook_page),
    path('addreader/', views.show_addreader_page),
    path('addrent/', views.show_addrent_page),
    path('showreaders/', views.show_readers),
    path('showrents/', views.show_rents),
    path('admin/', admin.site.urls),
]

