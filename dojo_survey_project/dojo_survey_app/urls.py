from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new_survey', views.new_survey),
    path('results', views.results)
]
