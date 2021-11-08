from django.urls import path
from short.views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('registration', registration),
    path('registr', registr),
    path('back', back),
    path('login_users', login_users),
    path('logout', do_logout),
    path('delete/<int:id>', delete),
    path('log_2', login_1),
    path('short', short),
]