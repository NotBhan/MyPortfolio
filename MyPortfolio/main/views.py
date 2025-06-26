from django.shortcuts import render, get_object_or_404
from .models import SkillCategory, Project

import logging

logger = logging.getLogger(__name__)

def index(request):
    context = {
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all(),
        'featured_projects': Project.objects.filter(featured=True).order_by('display_order')[:6]
    }
    return render(request, 'main/index.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'main/project_detail.html', {'project': project})

