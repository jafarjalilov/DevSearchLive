from django.shortcuts import render, redirect
from .models import Project
from .forms import CreateProjectForm
# Create your views here.

def projects_list(request):
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, 'projects/projects.html', context )

def single_project(request, pk):
    single_project = Project.objects.get(id = pk)
    tags = single_project.tags.all()
    reviews = single_project.review_set.all()
    context = { 'single_project': single_project, 'tags': tags, 'reviews': reviews }
    return render(request, 'projects/single_project.html', context)

def create_project(request):
    if request.method == 'POST':
        print("Form DATA: ", request.POST)
        form = CreateProjectForm(data=request.POST)
        if form.is_valid():
            newProject = form.save()
            return redirect('projects_list')
    else:
        form = CreateProjectForm()
    context = {'form':form}
    return render(request, 'projects/create.html', context)

def update_project(request, pk):
    project = Project.objects.get(id = pk)
    form = CreateProjectForm(instance=project)
    if request.method == 'POST':
        updatedProject = CreateProjectForm(data=request.POST, instance=project)
        updatedProject.save()
        return redirect('projects_list')
    context = {'form': form }
    return render(request, 'projects/create.html', context)

def delete_project(request, pk):
    project = Project.objects.get(id = pk)
    template = 'projects/delete.html'
    context = { 'project': project }

    if request.method == 'POST':
        project.delete()
        return redirect('projects_list')

    return render(request, template, context)