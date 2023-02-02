"""controle_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from client.views import client_view, home_view, client_view_10, client_view_after_2020
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", home_view, name="home"),
    path("client", client_view, name="client"),
    path("client10", client_view_10, name="client10"),
    path("client_2020", client_view_after_2020, name="client_2020"),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()
