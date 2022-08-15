from django.db import models
from ckeditor.fields import RichTextField
from django_cleanup import cleanup

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image = models.FileField(blank=True, null=True,verbose_name= "Makaleye Resim Ekleyin")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True,verbose_name="Yorum Tarihi")

    def __str__(self):
        self.comment_content

    class Meta:
        ordering = ["-comment_date"]

class CryptoCurrency(models.Model):
    id = models.IntegerField
    coin_no = models.CharField(max_length=10)
    coin_symbol = models.CharField(max_length=10)
    coin_name = models.CharField(max_length=100)
    coin_usd_price = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    coin_percent_change_24h = models.CharField(max_length=100)
    coin_percent_change_7d = models.CharField(max_length=100)
    coin_usd_market_cap = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    coin_usd_volume_24h = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    coin_circulating_supply = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated','-coin_usd_price']

    def __str__(self):
        return self.coin_symbol


class Currency(models.Model):
    code = models.CharField(max_length=10, verbose_name= 'Code')
    currencynumber = models.IntegerField(verbose_name="currencynumber")
    unit = models.IntegerField(verbose_name="unit")
    name = models.CharField(max_length=50, verbose_name="name")
    currency = models.CharField(max_length=50, verbose_name="currency")
    exchangedate = models.DateTimeField(verbose_name="exchangedate")
    buy = models.FloatField(verbose_name = "buy")
    sell = models.FloatField(verbose_name = "sell")
    crossrate = models.FloatField(verbose_name="crossrate")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-exchangedate',"name"]

class CurrencyList(models.Model):
    curr_id = models.IntegerField(verbose_name='curr_id')
    curr_code = models.CharField(max_length=100,verbose_name='curr_code')
    curr_name = models.CharField(max_length=100,verbose_name='curr_name')

    def __str__(self):
        return self.curr_name
    class Meta:
        ordering = ['curr_id']