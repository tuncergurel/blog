from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework import mixins
from rest_framework.filters import SearchFilter

from user.models import Profil,ProfilDurum
from currency.api.serializers import ProfilSerializers,ProfilDurumSerializers, ProfilFotoSerializers
from currency.api.permissions import OwnProfilOrReadOnly,StatusOwnerOrReadOnly




# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Register Successfuly...")
        return redirect("index")

    context = {
        "form": form
    }
    return render(request,"register.html",context)


    # if request.method == "POST":
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #
    #         newUser = User(username = username)
    #         newUser.set_password(password)
    #         newUser.save()
    #         login(request,newUser)
    #         return redirect("index")
    #
    #     context = {
    #         "form": form
    #     }
    #     return render(request,"register.html",context)
            
    # else:
    #     form = RegisterForm()
    #     context = {
    #         "form": form
    #     }
    #     return render(request,"register.html",context)
"""    form = RegisterForm()

    context = {
        "form":form
    }
    return render(request,"register.html",context)"""


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Username or Password is Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Login Success")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect("index")

# class ProfilList(generics.ListAPIView):
#     queryset = Profil.objects.all()
#     serializer_class = ProfilSerializers
#     permission_classes = [IsAuthenticated]


class ProfilViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializers
    permission_classes = [IsAuthenticated,OwnProfilOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['sehir']

class ProfilDurumViewSet(ModelViewSet):
    queryset = ProfilDurum.objects.all()
    serializer_class = ProfilDurumSerializers
    permission_classes = [IsAuthenticated,StatusOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profil =self.request.user
        serializer.save(user_profil=user_profil)

    def get_queryset(self):
        queryset = ProfilDurum.objects.all()
        username = self.request.query_params.get('username',None)
        if username is not None:
            queryset =queryset.filter(user_profil__user__username=username)
        return queryset






class ProfilPhotoUpdateView(generics.UpdateAPIView):
    permission_classes =  [IsAuthenticated]
    serializer_class = ProfilFotoSerializers

    def get_object(self):
        profil_obj = self.request.user.profil
        return profil_obj






