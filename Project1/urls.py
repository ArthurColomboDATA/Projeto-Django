"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import login_view, logout_view, home_view  # Importa as views diretamente

urlpatterns = [
    path("admin/", admin.site.urls),  # Página de administração do Django
    path("login/", login_view, name="login"),  # Página de login (página inicial)
    path("home/", home_view, name="home"),  # Página principal após login
    path("logout/", logout_view, name="logout"),  # Logout do usuário
]
