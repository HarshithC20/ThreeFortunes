from django.shortcuts import render, HttpResponse

# Create your views here.
def orders(request):
    return HttpResponse("Welcome to Orders page")