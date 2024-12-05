from django.shortcuts import render, HttpResponse

# Create your views here.

def kitchen(request):
    return HttpResponse("Welcome to Kitchen page")