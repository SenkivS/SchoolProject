from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
#from django.shortcuts import render
from webargs.djangoparser import use_args

from webargs.fields import Str

from .forms import CreateStudentForm
from .models import Students
from .utils import qs2html


def index(request):
    return HttpResponse('Welcome to LMS')


@use_args(
    {
        'name': Str(required=False),
        'surname': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Students.objects.all()
    if len(args) != 0 and args.get('name') or args.get('surname'):
        students = students.filter(
            Q(name=args.get('name')) | Q(surname=args.get('surname'))
        )

    html_form = '''
        <form method="get">
          <label for="name">First name:</label><br>
          <input type="text" id="name" name="name" placeholder="John"><br>
          <label for="surname">Last name:</label><br>
          <input type="text" id="surname" name="surname" placeholder="Doe"><br><br>
          <input type="submit" value="Submit">
        </form>
    '''


    # if 'name' in args:
    #     students = students.filter(name=args['name'])
    # if 'surname' in args:
    #     students = students.filter(surname=args['surname'])

    response = qs2html(students)
    return HttpResponse(html_form + response)


def create_student(request):
    # CreateStudentForm
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
    <form method = "post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
        <table>
            {form.as_table()}
        </table>
        <input type="submit" value="Submit">
    </form>
    '''
    return HttpResponse(html_form)
