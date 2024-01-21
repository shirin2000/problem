from django.shortcuts import render, redirect, get_object_or_404
from .models import Problems, MyProject, Blog
from .forms import ProblemForm, MyProjectForm, BlogForm

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
            return redirect('add_problem')  # Change 'success_page' to the desired URL name
    else:
        form = ProblemForm()

    return render(request, 'add_problem.html', {'form': form})

def add_to_my_project(request, problem_id):
    problem = Problems.objects.get(pk=problem_id)

    if request.method == 'POST':
        # Check if a MyProject instance with the same problem already exists
        existing_instance = MyProject.objects.filter(problem=problem.problem, sector=problem.sector).first()

        if existing_instance:
            # If already exists, show a message (you can customize this)
            return render(request, 'exist.html')
        else:
            # Create a new MyProject instance and save it to the database
            my_project_instance = MyProject(
                problem=problem.problem,
                sector=problem.sector
            )
            my_project_instance.save()

            # Redirect to the success page
            return redirect('success')

    return render(request, 'success.html', {'problem': problem, 'form': MyProjectForm()})

def myproject_view(request):
    myprojects = MyProject.objects.all()
    return render(request, 'myproject.html', {'myprojects': myprojects})


def remove_project(request, project_id):
    project = MyProject.objects.get(pk=project_id)
    project.delete()
    return redirect('myproject_view')



def solution_view(request, project_id):
    project = get_object_or_404(MyProject, id=project_id)

    if request.method == 'POST':
        form = MyProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()  # This will update the instance in the database
            return redirect('myproject_view')
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = MyProjectForm(instance=project)  # Pass the instance to pre-fill the form

    return render(request, 'solution.html', {'project': project, 'form': form})



def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_delete.html', {'blog': blog})


def success(request):
    return render(request, 'success.html')

def exist(request):
    return render(request, 'exist.html')
