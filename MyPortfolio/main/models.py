from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)  # Make sure this exists
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('design', 'Design'),
        ('other', 'Other')
    ])
    proficiency = models.IntegerField(default=80)  # percentage
    icon_class = models.CharField(max_length=50, blank=True)  # for Font Awesome

    def __str__(self):
        return self.name