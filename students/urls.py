from django.urls import path

from .views import index, get_students


urlpatterns = [
    path('', index),
    path('students/', get_students)
]
