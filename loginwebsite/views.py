from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse
from .models import User
import json
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    def get():
        serializer_class = UserSerializer
    def post(self, request):
        print(request.data)  

class UserRegister(viewsets.ModelViewSet):
    def post(self, request):
        print(request)    

def register_user(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = User()
        user.username = username
        user.password = password
        user.save()
    
    return render(req, 'register.html')
    # username = req.POST.get('username')
    # password = req.POST.get('password')
    # if username and password:
    #     user = User()
    #     user.username = username
    #     user.password = password
    #     user.save()
    #     return HttpResponse(json.dumps({"hey": "hey"}), content_type="application/json")
    # print(username + " e " + password)

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