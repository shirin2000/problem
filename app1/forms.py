from django import forms
from .models import Problems
from .models import MyProject
from .models import Blog


class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = ['solution', 'current_status', 'works_left']
        exclude = ['problem']


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'content', 'created_by']

