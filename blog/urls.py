"""blog URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from currency import views
from user import views as vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vi.loginUser, name="index"),
    path('rates/',views.Currency,name="rates"),
    path('cryptos/',views.Cryptos,name="cryptos"),
    path('cryptomoves/', views.cryptomoves, name="cryptomoves"),
    path('articles/', include("currency.urls")),
    path('user/', include("user.urls")),
    path('datatable/', include('datatable.urls')),

    path('api/', include('currency.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registiration/', include('rest_auth.registration.urls')),

]




