from rest_framework import serializers
from currency.models import CurrencyList, Currency, CryptoCurrency
from user.models import Profil,ProfilDurum

#Modelden serializer yaratmak
class CurrencyListSerializer_Model(serializers.ModelSerializer):
    class Meta:
        models = CurrencyList
        fields = '__all__'


# Standart serializer
class CurrencyListSerializer(serializers.Serializer):
    curr_id = serializers.IntegerField()
    curr_code = serializers.CharField()
    curr_name = serializers.CharField()

    def create(self, validated_data):
        return CurrencyList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.curr_code = validated_data.get('curr_id',instance.curr_code)
        instance.curr_name = validated_data.get('curr_name',instance.curr_name)

        instance.save()
        return instance

    def validate(self, data): #kuralların (veri doğrulama işlemlerinin) yapıldığı yer
        if data['curr_code'] == data['curr_name']:
            raise serializers.ValidationError('Kur kodu ve kur ismi aynı olamaz')
        return data


class CurrencySerializer(serializers.Serializer):
    code = serializers.CharField()
    currencynumber = serializers.IntegerField()
    unit = serializers.IntegerField()
    name = serializers.CharField()
    currency = serializers.CharField()
    exchangedate = serializers.DateTimeField()
    buy = serializers.FloatField()
    sell = serializers.FloatField()
    crossrate = serializers.FloatField()

    def create(self, validated_data):
        return Currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code',instance.code)
        instance.currencynumber = validated_data.get('currencynumber',instance.currencynumber)
        instance.unit = validated_data.get('unit',instance.unit)
        instance.name = validated_data.get('name',instance.name)
        instance.currency = validated_data.get('currency',instance.currency)
        instance.exchangedate = validated_data.get('exchangedate',instance.exchangedate)
        instance.buy = validated_data.get('buy',instance.buy)
        instance.sell = validated_data.get('sell',instance.sell)
        instance.crossrate = validated_data.get('crossrate',instance.crossrate)

        instance.save()
        return instance

    def validate(self, data): #kuralların (veri doğrulama işlemlerinin) yapıldığı yer
        pass

class CryptoCurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField
    coin_no = serializers.CharField()
    coin_symbol = serializers.CharField()
    coin_name = serializers.CharField()
    coin_usd_price = serializers.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    coin_percent_change_24h = serializers.CharField()
    coin_percent_change_7d = serializers.CharField()
    coin_usd_market_cap = serializers.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    coin_usd_volume_24h = serializers.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    coin_circulating_supply = serializers.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    last_updated = serializers.DateTimeField()

    def create(self, validated_data):
        return CryptoCurrency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.coin_no = validated_data.get('coin_no', instance.coin_no)
        instance.coin_symbol = validated_data.get('coin_symbol', instance.coin_symbol)
        instance.coin_name = validated_data.get('coin_name', instance.coin_name)
        instance.coin_usd_price = validated_data.get('coin_usd_price', instance.coin_usd_price)
        instance.coin_percent_change_24h = validated_data.get('coin_percent_change_24h', instance.coin_percent_change_24h)
        instance.coin_percent_change_7d = validated_data.get('coin_percent_change_7d', instance.coin_percent_change_7d)
        instance.coin_usd_market_cap = validated_data.get('coin_usd_market_cap', instance.coin_usd_market_cap)
        instance.coin_usd_volume_24h = validated_data.get('coin_usd_volume_24h', instance.coin_usd_volume_24h)
        instance.coin_circulating_supply = validated_data.get('coin_circulating_supply', instance.coin_circulating_supply)
        instance.last_updated = validated_data.get('last_updated', instance.last_updated)

        instance.save()
        return instance

    def validate(self, data): #kuralların (veri doğrulama işlemlerinin) yapıldığı yer
        pass

class ProfilSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Profil
        fields = '__all__'

class ProfilFotoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = ['foto']


class ProfilDurumSerializers(serializers.ModelSerializer):
    user_profil = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfilDurum
        fields = '__all__'