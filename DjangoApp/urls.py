"""
URL configuration for DjangoApp project.

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
from crud import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Página principal será el login
    path('index/', views.index, name='index'),  # Página CRUD
    path('add/', views.add_user, name='add_user'),  # Agregar usuario
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),  # Editar usuario
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),  # Eliminar usuario
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
]