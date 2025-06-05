from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    titleImage = models.ImageField(upload_to='project_images/', default='coming.jpg')
    category = models.ForeignKey('Category', related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/', default='noProject.jpg')

    def __str__(self):
        return f"Image for {self.project.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
        class Meta:
            ordering = ['name']

