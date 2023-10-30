"""
URL configuration for StudentHelper project.

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
from rest_framework.routers import SimpleRouter
from Knagu import views
from Knagu.views import index_page, gen, list_of_info, todo, add
from Knagu.views import get_data
from  Knagu.views import way
from  Knagu.views import templ

urlpatterns = [
    path('submit/', views.get_data, name='submit'),
    path('', index_page),
    path('admin/', admin.site.urls),
    path('basa/templ', templ),
    path('basa/gen', gen),
    path('basa/gen/list', list_of_info),
    path('basa/way', way),
    path('basa/todo',todo),
    path('basa/add',add),






]

