from django.shortcuts import render, redirect, get_object_or_404
from .models import Problems, MyProject
from .forms import ProblemForm, MyProjectForm

def home(request):
    return render(request, 'home.html')

def agriculture(request):
    problems = Problems.objects.filter(sector='agriculture')
    return render(request, 'agriculture.html',{'problems': problems})

def education(request):
    problems = Problems.objects.filter(sector='education')
    return render(request, 'education.html', {'problems': problems})

def health(request):
    problems = Problems.objects.filter(sector='health')
    return render(request, 'health.html', {'problems': problems})

def technology(request):
    problems = Problems.objects.filter(sector='technology')
    return render(request, 'technology.html', {'problems': problems})

def environment(request):
    problems = Problems.objects.filter(sector='environment')
    return render(request, 'environment.html', {'problems': problems})

def transportation(request):
    problems = Problems.objects.filter(sector='transportation')
    return render(request, 'transportation.html', {'problems': problems})

def fashion(request):
    problems = Problems.objects.filter(sector='fashion')
    return render(request, 'fashion.html', {'problems': problems})

def sports(request):
    problems = Problems.objects.filter(sector='sports')
    return render(request, 'sports.html', {'problems': problems})

def research(request):
    problems = Problems.objects.filter(sector='research')
    return render(request, 'research.html', {'problems': problems})
# Add other views as needed...


def problem_detail(request, problem_id):
    problem = Problems.objects.get(pk=problem_id)
    return render(request, 'problem_detail.html', {'problem': problem})

def add_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added!')
            return redirect('add_problem')  # Change 'success_page' to the desired URL name
    else:
        form = ProblemForm()

    return render(request, 'add_problem.html', {'form': form})

def add_to_my_project(request, problem_id):
    problem = Problems.objects.get(pk=problem_id)

    if request.method == 'POST':
            # Create a new MyProject instance and save it to the database
        my_project_instance = MyProject(
            problem=problem.problem
        )
        my_project_instance.save()

        return redirect('agriculture')  # Redirect to the agriculture page, adjust as needed

    return render(request, 'agriculture.html', {'problem': problem, 'form': MyProjectForm()})


def myproject_view(request):
    myprojects = MyProject.objects.all()
    return render(request, 'myproject.html', {'myprojects': myprojects})