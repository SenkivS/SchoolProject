from django.http import HttpResponse
from django.shortcuts import render

from .models import Students
from .utils import qs2html





def index(request):
    return HttpResponse('Welcome to LMS')


def get_students(request):
    students = Students.objects.order_by('name')
    response = qs2html(students)
    return HttpResponse(response)
