from django import forms
from .models import Project, ProjectImage


from django import forms
from .models import Project, ProjectImage
from django.forms import modelformset_factory

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'titleImage','category']

class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']

ProjectImageFormSet = modelformset_factory(ProjectImage, form=ProjectImageForm, extra=3, can_delete=True)



# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name']

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result

# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = ProjectImage
#         fields = ['image']
    
