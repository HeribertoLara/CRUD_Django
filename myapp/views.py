from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from django.shortcuts import render, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):
    title = "welcome to django course!!"
    return render(request,"index.html", {'title':title})

def hello(request, username):
    return HttpResponse("<h2>Hello %s<h2>" % username)

def about( request ):
    username = "hlara"
    return render(request, "About.html", {'username':username})

def projects( request ):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {'projects': projects})

def tasks( request ):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {'tasks': tasks})

def create_task( request ):
    if request.method == "GET":
        return render(request, "tasks/create-task.html",{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.GET['description'], project_id=2)
        return redirect('tasks')

def create_project( request ):
    if request.method == "GET":
        return render(request, "projects/create_project.html",{
            'form':CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST["name"])
        redirect('projects')
        return render(request, 'projects/create_project.html', { 
                                                                    'form':CreateNewProject()
                                                                }) 
def detail_project( request, id ):
    project = get_object_or_404(Project, id=id) 
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks' : tasks
    })