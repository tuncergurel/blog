from django.urls import path, include
from currency.api import views as api_views
from user.views import ProfilViewSet,ProfilDurumViewSet,ProfilPhotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiller',ProfilViewSet)
router.register(r'durum',ProfilDurumViewSet,basename="durum")


profil_list = ProfilViewSet.as_view({'get':'list'})
profil_detay = ProfilViewSet.as_view({'get':'retrieve'})


#FONKSİYON TEMELLİ
# urlpatterns = [
#     path('currencies/', api_views.currenct_list_create_view, name="currency_list"),
#     path('currencies/<int:pk>', api_views.current_detail_api_view, name="currency_detail"),
# ]

#CLASS TEMELLİ

urlpatterns = [
    path('currencieslist/', api_views.CurrentListCreateView.as_view(), name="currency_list"),
    path('currencieslist/<int:pk>', api_views.CurrentListDetailView.as_view(), name="currency_detail"),
    path('currencies/', api_views.CurrentCreateView.as_view(), name="currencies"),
    path('currencies/<int:pk>', api_views.CurrentDetailView.as_view(), name="currencies_details"),
    path('cryptosCurr/', api_views.CryptoCurrencyCreateView.as_view(), name="cryptosCurr"),
    path('cryptosCurr/<int:pk>', api_views.CryptoCurrencyDetailView.as_view(), name="cryptos_details"),

    path('kullanici/', profil_list, name="profiller"), #user modülü altından alındı
    path('kullanici/<int:pk>', profil_detay, name="profil_detay"), #user modülü altından alındı

    path("",include(router.urls)),
    path("profil_photo/",ProfilPhotoUpdateView.as_view() ,name = "Profil-foto"),
]









