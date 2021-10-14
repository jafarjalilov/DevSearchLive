from django.shortcuts import render

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

    context = { 'projects': projectsList }
    return render(request, 'projects/projects.html', context )

def single_project(request, pk):
    return render(request, 'projects/single_project.html', {"pk":pk})