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
    path('add/', views.add_problem, name='add_problem'),
    path('add_to_my_project/<int:problem_id>/', views.add_to_my_project, name='add_to_my_project'),
    path('myproject/', views.myproject_view, name='myproject'),
    # Add other paths as needed...
]

