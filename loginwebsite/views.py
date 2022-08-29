from urllib import request
from django.shortcuts import render, HttpResponse
from .models import User
from django.contrib.auth import authenticate, login

def register_user(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = User()
        user.username = username
        user.password = password
        user.save()
    
    return render(req, 'register.html')

def login_user(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    session_id = req.session._get_or_create_session_key()

    users = User.objects.filter(session_id=session_id)
    for user in users:
        user.session_id = ""
        user.save()

    try:
        user = User.objects.get(username=username, password=password)
    except:
        return render(req, 'login.html')

    user.session_id = session_id
    user.save()
    return render(req, 'index.html', {'loggedUser': user.username})

def main_menu(req):
    users = User.objects.filter(session_id=req.session._get_or_create_session_key())

    for user in users:
        return render(req, 'index.html', {'loggedUser': user.username})
    
    return render(req, 'index.html')