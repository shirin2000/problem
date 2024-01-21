"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home/', views.home,name='home'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('education/', views.education, name='education'),
    path('health/', views.health, name='health'),
    path('technology/', views.technology, name='technology'),
    path('environment/', views.environment, name='environment'),
    path('transportation/', views.transportation, name='transportation'),
    path('fashion/', views.fashion, name='fashion'),
    path('sports/', views.sports, name='sports'),
    path('research/', views.research, name='research'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('add_problem/', views.add_problem, name='add_problem'),
    path('add_to_my_project/<int:problem_id>/', views.add_to_my_project, name='add_to_my_project'),
    path('myproject/', views.myproject_view, name='myproject'),
    path('remove_project/<int:project_id>/', views.remove_project, name='remove_project'),
    path('myproject/', views.myproject_view, name='myproject_view'),
    path('solution/<int:project_id>/', views.solution_view, name='solution_view'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/new/', views.blog_new, name='blog_new'),
    path('blog/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('success/', views.success, name='success'),
    path('exist/', views.exist, name='exist'),

    # Add other paths as needed...
]

