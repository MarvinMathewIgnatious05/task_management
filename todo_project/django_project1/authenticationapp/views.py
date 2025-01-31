
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# def login_in(request,user):
#     return HttpResponse(user)
# @login_required(login_url="login_page")
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        login_required(request,user)
        if user:
            print("login alreadyyyyyyyyyyyyyyyy",user)
            messages.success(request," successfully login")
            return redirect("add_task")

            # return login_in(request, user)
        else:
            print("invalid username or password")

    return render(request, "login.html")
# @login_required(login_url="login_page")
def registration(request):
    if request.method=='POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
            user.save()
            return redirect("login_page")


        else:
            messages.success(request, "password not match")

    return render(request,"registration_form.html")


def logout_user(request):
    logout(request)










