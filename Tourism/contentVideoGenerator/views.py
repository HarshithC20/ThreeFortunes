from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Tourism home page!!")

def contentSource(request):
    return render(request, "source.html")

def place(request):
    return render(request, "place.html")