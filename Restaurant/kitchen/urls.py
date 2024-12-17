from django.urls import path, include
from .views import kitchen
urlpatterns = [
    path('', kitchen, name='Kitchen View'),

]