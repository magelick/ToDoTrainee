from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Registration Project model in admin panel
    """


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Registration Task model in admin panel
    """
