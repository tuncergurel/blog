from django.contrib import admin
from currency.models import Currency, CurrencyList, CryptoCurrency
from user.models import Profil,ProfilDurum


# Register your models here.
admin.site.register(Currency)
admin.site.register(CurrencyList)
admin.site.register(CryptoCurrency)

admin.site.register(Profil)
admin.site.register(ProfilDurum)





