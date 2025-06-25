from django.contrib import admin
from . import models
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # columns to show
    search_fields = ('name', 'age','email')        # search bar
    list_filter = ('age',)                 
    
admin.site.register(models.Student, StudentAdmin)  # Register the Student model with the custom admin interface)
