from django.urls import path, include
from .views import home, contentSource, place
urlpatterns = [
    path('home/', home, name='Home View'),
    path('source/', contentSource, name='Source View'),
    path('place/', place, name='Place View'),

]