from django.urls import path
from .views import index, project_detail

urlpatterns = [
    path('', index, name='home'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
]