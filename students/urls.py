from django.urls import path

from students.views import index

urlpatterns = [
    path('', index)
]