from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "currency"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('currency/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('delete/<int:id>', views.deleteArticle, name="delete"),
    # path('cryptomoves/', views.cryptomoves, name="cryptomoves"),
    path('comment/<int:id>', views.addComment, name="comment"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
