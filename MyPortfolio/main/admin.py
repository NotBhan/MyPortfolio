from django.contrib import admin
from .models import SkillCategory, Skill, Project
from django import forms
from django.db import models


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'proficiency', 'display_order')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ('name', 'icon', 'display_order')
    list_editable = ('display_order',)

class ProjectForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    updated_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )

    class Meta:
        model = Project
        fields = '__all__'

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('title', 'featured', 'display_order', 'created_at', 'updated_at')
    list_filter = ('featured', 'technologies', 'created_at')
    list_editable = ('featured', 'display_order')
    filter_horizontal = ('technologies',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'featured', 'display_order')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
        }),
        ('Content', {
            'fields': ('short_description', 'long_description', 'image')
        }),
        ('Links', {
            'fields': ('demo_url', 'source_url')
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
    )


    
admin.site.register(Project, ProjectAdmin)