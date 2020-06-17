"""ramais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/ramais/')),
    path('ramais/', views.lista_ramais),
    path('delete/<int:id_ramal>',views.delete_ramal),
    path('emails/', views.lista_emails),
    path('emails/edicao/', views.ed_ramal),
    path('emails/edicao/submit', views.submit_edicao),
    path('emails/delete/<int:id_ramal>',views.delete_email),
    path('empresas/', views.lista_empresas),
    path('login/', views.login_edicao),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_edicao),
    path('ramais/edicao/', views.ed_ramal),
    path('ramais/edicao/submit', views.submit_edicao),
    path('ramais/edicao/setor/', views.add_setor),
    path('ramais/edicao/setor/submit', views.submit_setor),
    path('api/', include('app.urls')),
]
