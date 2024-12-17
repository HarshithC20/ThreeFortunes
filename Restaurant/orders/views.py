from django.shortcuts import render, HttpResponse

# Create your views here.
def menu(request):
    return render(request, 'menu.html')