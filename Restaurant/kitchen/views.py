from django.shortcuts import render

# Create your views here.
def kitchen(request):
    return render(request, 'kitchen.html')
