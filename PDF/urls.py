from django.urls import path
from .views import *

urlpatterns = [
    path('', accept, name='accept'),
    path('resume/<id>', resume, name='resume'),
    path('list/', list, name='list'),
]