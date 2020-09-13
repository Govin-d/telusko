from django.urls import path
import os
print(os.getcwd())
from . import views

urlpatterns = [
    path('',views.home, name='home')

]
