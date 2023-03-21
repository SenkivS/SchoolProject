from django.urls import path

from .views import index, get_students, create_student

urlpatterns = [
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student),
]
