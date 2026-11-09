from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lost_and_found_index'),
]
