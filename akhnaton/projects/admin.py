from django.contrib import admin

from django import forms

from .models import Category, ContactMessage, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Category)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')

