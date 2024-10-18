from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('encryption.html', views.encryption, name='encryption'),
    path('decryption.html', views.decryption, name='decryption'),
    path('your-url/', views.encryption, name='encryption'),
    path('your-url/', views.decryption, name='decryption'),
]