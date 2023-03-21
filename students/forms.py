from django import forms
from .models import Students

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            'name',
            'surname',
            'email',
            'birthday'
        ]