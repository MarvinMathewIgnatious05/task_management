import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_page_view(request):
    return HttpResponse("welcome")
    # return render(request,"text.html",{{'name':'mark'}})



# def task_list(request):
#
#     tasks = [
#         Task(task_title="", task_complete=True),
#         Task(task_title="", task_complete=False)
#     ]
#
#     for task in tasks:
#         task.save()
#
#     return render(request, "task_list.html", {"task_list":tasks })



# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'task_list.html', {'task_list': tasks})
#
#
# def add_task(request):
#     if request.method == 'POST':
#         title = request.POST['task_title']
#         complete = request.POST['task_complete']
#         description = request.POST['task_description']
#         if title:
#             Task.objects.create(task_title=title, task_complete=complete, task_description=description, user= request.user)
#         return redirect('add_task')
#     return render(request, 'task_list.html')



@login_required(login_url="login_page")
def  add_task(request):

    if request.method == 'POST':
        title = request.POST.get('task_title')
        complete = request.POST.get('task_complete')
        description = request.POST.get('task_description')



        if title:
            Task.objects.create(task_title = title,task_complete = complete,task_description = description, user = request.user)
            print("added success")
            messages.success(request," Task successfully added ")
            return redirect("add_task")

    tasks = Task.objects.filter(user = request.user).values()
    print(tasks)
    return render(request,"add_task.html",{"task_list":tasks})
    # return render(request,"task_list.html",{"task_list":tasks})



@login_required(login_url="login_page")
def delete_task(request,id):

    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request,"deleted successfully")

    return redirect("add_task")

@login_required(login_url="login_page")
def view_task(request,id):
    print(id,"id")
    # return HttpResponse("hi")
    task = Task.objects.get(id=id)
    return render(request,"view_task.html",{"task_list":task})

def edit_task(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('task_title')
        complete = request.POST.get('task_complete')
        description = request.POST.get('task_description')
        task.task_title = title
        task.task_complete = complete
        task.task_description = description
        task.save()

        return redirect("add_task")

    return render(request, "edit_task.html", {"task_list": task})

    # return render(request,"edit_task.html",{"task_list":task})

# def delete_view(request,id):
#     task = Task.objects.get(id=id)
#     task.delete()
#
#     return redirect("view_task")












def get_time(request):
    return HttpResponse(f"""
    <h1>today time</h1>
    <p>today time is  {datetime.datetime.now()} </p>""")


def sum_num(request):

    try:
        a=request.GET.get('x', 0)
        b = request.GET.get('y',0)
        c = int(a) + int(b)
        print("sum of number :", c)
        return HttpResponse(f"sum of number {c}")
    except Exception as e:
        print(f"error{e}")
        return  HttpResponse("data error")



def hi_bat(request):
    return HttpResponse(datetime.datetime.now())


# def factorial(request):
#     num = 3
#     fact = 1
#     for i in range(1,num+1):


