from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectImageFormSet, ProjectForm

from .models import Category, Project, ProjectImage


# Create your views here.

def add_project(request):
    if request.method == 'POST':
        form =  ProjectForm(request.POST,request.FILES)
        images = request.FILES.getlist('images')

        if form.is_valid():
            project = form.save()
            for image_file in images:
                ProjectImage.objects.create(project=project,image=image_file)
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request,'projects/add.html',{'form':form})


def edit_project(request, id):
    project = get_object_or_404(Project,id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        images = request.FILES.getlist('images')
        if form.is_valid():
            form.save()
            for image_file in images:
                ProjectImage.objects.create(project=project,image=image_file)
            return redirect('project_detail',id=project.id)
    else:
        form = ProjectForm(instance=project)

    images = project.images.all()
    return render(request,'projects/edit.html',{'form':form, 'images':images,'project':project})


from django.views.decorators.http import require_POST

@require_POST
def delete_project_image(request, image_id):
    image = get_object_or_404(ProjectImage, id=image_id)
    project_id = image.project.id
    image.delete()
    return redirect('edit_project', id=project_id)



def index(request):
    projects = Project.objects.all()[:3]
    return render(request,'projects/index.html',{'projects':projects})


def project_list(request):
    category_id = request.GET.get('category')  # e.g., ?category=2
    categories = Category.objects.all()

    if category_id:
        projects = Project.objects.filter(category_id=category_id)
    else:
        projects = Project.objects.all()

    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    })


def project_detail(request, id):
    project = get_object_or_404(Project,id=id)
    images = project.images.all()
    return render(request, 'projects/project_detail.html',{'project':project, 'images':images})

def about(request):
    return render(request,'projects/about.html')

def tools(request):
    return render(request,'projects/tools.html')

def consultants(request):
    return render(request,'projects/consultants.html')

def subContractors(request):
    return render(request,'projects/sub-contractors.html')

def certificates_of_appreciation(request):
    return render(request,'projects/certificates-of-appreciation.html')

