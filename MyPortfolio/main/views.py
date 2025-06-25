from django.shortcuts import render
from .models import Project, Skill

# Create your views here.


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    skills = Skill.objects.all()
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'main/index.html', context)