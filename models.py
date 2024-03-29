# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# class CryptoCurrency(models.Model):
#     id = models.IntegerField
#     coin_no = models.CharField(max_length=10)
#     coin_symbol = models.CharField(max_length=10)
#     coin_name = models.CharField(max_length=10)
#     coin_usd_price = models.DecimalField(18,4)
#     coin_percent_change_24h = models.CharField
#     coin_percent_change_7d = models.CharField
#     coin_usd_market_cap = models.DecimalField
#     coin_usd_volume_24h = models.DecimalField
#     coin_circulating_supply = models.DecimalField,
#     last_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.coin_symbol
#
# class Currency(models.Model):
#     id = models.IntegerField
#     code = models.CharField(max_length=10)
#     currencynumber = models.CharField(max_length=10)
#     unit = models.CharField(max_length=10)
#     name = models.CharField(max_length=100)
#     currency = models.CharField(max_length=100)
#     exchangedate = models.DateTimeField
#     buy = models.DecimalField(18,4)
#     sell = models.DecimalField(18,4)
#     crossrate = models.DecimalField(18,4)
#
#     def __str__(self):
#         return self.code
#
#
# class CurrencyList(models.Model):
#     curr_id = models.IntegerField
#     curr_code = models.CharField(max_length=100)
#     curr_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.curr_name


class ArticleArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField()
    author = models.ForeignKey('AuthUser', models.DO_NOTHING)
    article_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_article'


class ArticleComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment_author = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField()
    article = models.ForeignKey(ArticleArticle, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_comment'


class ArticleCurrency(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10)
    currencynumber = models.IntegerField()
    unit = models.IntegerField()
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    exchangedate = models.DateTimeField()
    buy = models.FloatField()
    sell = models.FloatField()
    crossrate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'article_currency'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Getorders(models.Model):
    salesorderid = models.AutoField()
    revisionnumber = models.IntegerField(blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    shipdate = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    onlineorderflag = models.IntegerField(blank=True, null=True)
    orderaccountnumber = models.CharField(max_length=50, blank=True, null=True)
    customerid = models.AutoField(blank=True, null=True)
    salespersonid = models.AutoField(blank=True, null=True)
    territoryid = models.AutoField(blank=True, null=True)
    billtoaddressid = models.AutoField(blank=True, null=True)
    shiptoaddressid = models.AutoField(blank=True, null=True)
    shipmethodid = models.AutoField(blank=True, null=True)
    creditcardid = models.AutoField(blank=True, null=True)
    currencyrateid = models.AutoField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    taxamt = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    freight = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    totaldue = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    modifieddate = models.DateField(blank=True, null=True)
    personid = models.AutoField(blank=True, null=True)
    storeid = models.AutoField(blank=True, null=True)
    customeraccountnumber = models.CharField(max_length=50, blank=True, null=True)
    businessentityid = models.AutoField(blank=True, null=True)
    persontype = models.CharField(max_length=5, blank=True, null=True)
    title = models.CharField(max_length=10, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    emailpromotion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'getorders'


class Getordersdetails(models.Model):
    salesorderid = models.AutoField()
    purchaseordernumber = models.CharField(max_length=50, blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    personid = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    productname = models.CharField(max_length=200, blank=True, null=True)
    productnumber = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    safetystocklevel = models.IntegerField(blank=True, null=True)
    standardcost = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    listprice = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    sizeunitmeasurecode = models.CharField(max_length=10, blank=True, null=True)
    weightunitmeasurecode = models.CharField(max_length=10, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    productsubcategoryid = models.IntegerField(blank=True, null=True)
    productmodelid = models.IntegerField(blank=True, null=True)
    orderqty = models.IntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    unitpricediscount = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    linetotal = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    businessentityid = models.IntegerField(blank=True, null=True)
    accountnumber = models.CharField(max_length=50, blank=True, null=True)
    vendorname = models.CharField(max_length=250, blank=True, null=True)
    activeflag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'getordersdetails'
