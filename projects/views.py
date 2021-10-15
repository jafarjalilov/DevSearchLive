from django.shortcuts import render
from .models import Project
# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects_list(request):
    projects = Project.objects.all()
    print(projects)
    context = { 'projects': projects }
    return render(request, 'projects/projects.html', context )

def single_project(request, pk):
    single_project = Project.objects.get(id = pk)
    tags = single_project.tags.all()
    reviews = single_project.review_set.all()
    context = { 'single_project': single_project, 'tags': tags, 'reviews': reviews }
    return render(request, 'projects/single_project.html', context)