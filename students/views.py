from django.shortcuts import render
from .models import Students
#from django.http import HttpResponse


def index(request):
    students = Students.objects.all()
    student_dict = {
        'students': students
    }
    return render(request, 'index.html', student_dict)
