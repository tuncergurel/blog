from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "datatable"


urlpatterns = [
    path('get_currencyList/', views.get_currencyList, name="get_currencyList"),

]