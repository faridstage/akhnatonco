from django.contrib import admin

from django import forms

from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectImage)

