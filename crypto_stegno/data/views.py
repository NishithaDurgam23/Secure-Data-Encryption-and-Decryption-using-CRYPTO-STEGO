from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def encryption(request):
    return render(request, 'encryption.html')

def decryption(request):
    return render(request, 'decryption.html')

