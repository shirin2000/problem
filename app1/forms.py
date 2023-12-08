from django import forms
from .models import Problems
from .models import MyProject

class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = '__all__'


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = '__all__'

