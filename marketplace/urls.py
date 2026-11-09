from django.urls import path
from templates.marketplace import views

urlpatterns = [
    path('', views.index, name='marketplace_index'),
]
