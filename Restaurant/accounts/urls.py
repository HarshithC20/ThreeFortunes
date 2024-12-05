from django.urls import path, include
from .views import register_user, login_user, logout_user, items

urlpatterns = [
    path('register/', register_user, name='Signup View'),
    path('login/', login_user, name='Signin View'),
    path('items/', items, name='Items View'),

]