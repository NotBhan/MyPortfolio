from django.db import models
from django.utils import timezone
import bleach
from django.urls import reverse

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, 
                          help_text="Font Awesome icon class (e.g. 'fa-html5')")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, 
                               related_name='skills')
    proficiency = models.PositiveIntegerField(default=75,
                                            help_text="Proficiency percentage (0-100)")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)
    technologies = models.ManyToManyField(Skill)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})
    
