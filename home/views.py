from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page():
    return HttpResponse('home.html')