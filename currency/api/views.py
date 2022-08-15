from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework import generics
from currency.models import CurrencyList,Currency, CryptoCurrency
from currency.api.serializers import CurrencyListSerializer,CurrencySerializer, CryptoCurrencySerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import permissions
from currency.api.permissions import IsAdminUserOrReadOnly, IsUserOrReadOnly
from currency.api.pagination import SmallPagination, LargePagination

#Concrete view ile yapılışı
class CurrentListCreateView(generics.ListCreateAPIView):
    queryset = CurrencyList.objects.all()
    serializer_class = CurrencyListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #permission_classes = [IsUserOrReadOnly] # sadece işlemi yapan kullanıcı düzeltebilsin diye
    pagination_class = SmallPagination

class CurrentListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrencyList.objects.all()
    serializer_class = CurrencyListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentCreateView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()[:23]
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LargePagination

class CurrentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CryptoCurrencyCreateView(generics.ListCreateAPIView):
    queryset = CryptoCurrency.objects.all()[:50]
    serializer_class = CryptoCurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LargePagination

class CryptoCurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





# GenericAPIview ile yapılışı
# class CurrentListCreateView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = CurrencyList.objects.all()
#     serializer_class = CurrencyListSerializer
#
#     #list
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     #create
#     def post(self,request,*args,**kwargs):
#         return self.create(self,request,*args,**kwargs)



# CLASS TEMELLİ
# class CurrentListCreateView(APIView):
#     def get(self,request):
#         currencieslist = CurrencyList.objects.all()
#         serializer = CurrencyListSerializer(currencieslist,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = CurrencyListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class CurrentListDetailView(APIView):
#     def get_object(self,pk):
#         currency_instance = get_object_or_404(CurrencyList, pk=pk)
#         return currency_instance
#
#     def get(self,request,pk):
#         instance = self.get_object(pk=pk)
#         serializer = CurrencyListSerializer(instance)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#         instance = self.get_object(pk=pk)
#         serializer = CurrencyListSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         instance = self.get_object(pk=pk)
#         instance.delete()
#         return Response(
#             {
#                 'islem': {
#                     'code': 204,
#                     'message': f'{pk} numralı kur silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# class CurrentCreateView(APIView):
#     def get(self,request):
#         currencies = Currency.objects.all()
#         serializer = CurrencySerializer(currencies,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = CurrencySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class CurrentDetailView(APIView):
#     def get_object(self,pk):
#         currency_instance = get_object_or_404(Currency, pk=pk)
#         return currency_instance
#
#     def get(self,request,pk):
#         instance = self.get_object(pk=pk)
#         serializer = CurrencySerializer(instance)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#         instance = self.get_object(pk=pk)
#         serializer = CurrencySerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         instance = self.get_object(pk=pk)
#         instance.delete()
#         return Response(
#             {
#                 'islem': {
#                     'code': 204,
#                     'message': f'{pk} numralı kur silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# class CryptoCurrencyCreateView(APIView):
#     def get(self, request):
#         cryptosCurr = CryptoCurrency.objects.all()
#         serializer = CryptoCurrencySerializer(cryptosCurr, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CryptoCurrencySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class CryptoCurrencyDetailView(APIView):
#     def get_object(self, pk):
#         cryptosCurr = get_object_or_404(CryptoCurrency, pk=pk)
#         return cryptosCurr
#
#     def get(self, request, pk):
#         instance = self.get_object(pk=pk)
#         serializer = CryptoCurrencySerializer(instance)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         instance = self.get_object(pk=pk)
#         serializer = CryptoCurrencySerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         instance = self.get_object(pk=pk)
#         instance.delete()
#         return Response(
#             {
#                 'islem': {
#                     'code': 204,
#                     'message': f'{pk} numaralı kur silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# FONKSİYON TEMELLİ

# @api_view(['GET','POST'])
# def currenct_list_create_view(request):
#     if request.method == 'GET':
#         currencies = CurrencyList.objects.all()
#         serializer = CurrencyListSerializer(currencies,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CurrencyListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def current_detail_api_view(request,pk):
#     try:
#         current_instance = CurrencyList.objects.get(pk=pk)
#     except CurrencyList.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code' : 404,
#                     'message': f'Böyle bir id ile {pk} kur bilgisi bulunamadı'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
#     if request.method == 'GET':
#         serializer = CurrencyListSerializer(current_instance)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CurrencyListSerializer(current_instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         current_instance.delete()
#         return Response(
#             {
#                 'islem': {
#                     'code': 204,
#                     'message': f'{pk} numralı kur silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )
#
#
#
#










