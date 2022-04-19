"""halal_all_you_can_eat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from re import template
from django import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from coreapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('resturant/sign_in/', auth_views.LoginView.as_view(template_name='resturant/sign_in.html'), name="resturant_sign_in"),
    path('resturant/sign_out/', auth_views.LogoutView.as_view(next_page='/'), name="resturant_sign_out"),
    path('resturant/home/', views.resturant_home, name="resturant_home"),

]
