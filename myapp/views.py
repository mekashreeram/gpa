from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Marks
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def home(req):
  return render(req, "home.html")



lst = []
def index(req):
  current_user = req.user
  obj = Marks()
  if req.method == "POST":
    obj.name = req.POST["subName"]
    obj.credit = float(req.POST["credit"])
    obj.grade = int(req.POST["grade"])
    obj.factor = current_user.username
    obj.save()

    total = 0
    credsum = 0
    gpa = 0
    lst = Marks.objects.filter(factor = current_user.username)
    for i in range(0, len(lst)):
      total = total + (lst[i].credit * lst[i].grade)

    for i in range(0, len(lst)):
      credsum = credsum + lst[i].credit

    gpa = total / credsum
    return render(req, 'index.html', {"lst": lst, "gpa": gpa, "name": current_user} )
  
  else:
    if req.user.is_authenticated:
      total = 0
      credsum = 0
      gpa = 0
      lst = Marks.objects.filter(factor = current_user.username)
      for i in range(0, len(lst)):
        total = total + (lst[i].credit * lst[i].grade)

      for i in range(0, len(lst)):
        credsum = credsum + lst[i].credit

      if credsum == 0:
        credsum = 1
      
      gpa = total / credsum
      return render(req, 'index.html', {"lst": lst, "gpa": gpa, "name": current_user} )
    else:
      return HttpResponse("User not authenticated")
  
  
  

def register(req):
  if req.method == "POST":
    first_name = req.POST["first_name"]
    last_name = req.POST["last_name"]
    username = req.POST["username"]
    email = req.POST["email"]
    password1 = req.POST["password1"]
    password2 = req.POST["password2"]

    if password1 == password2:
      if User.objects.filter(username=username).exists():
        messages.info(req, "Username already taken")
      elif User.objects.filter(email=email).exists():
        messages.info(req, "email already taken")
      else:
        user = User.objects.create_user(username= username, password= password1, first_name= first_name, last_name= last_name, email= email)
        user.save()
        messages.info(req, "User created successfully")
        return redirect("/login")
    
    else:
      messages.info(req, "password not matched")

    return redirect("register")

  else:
    return render(req, "register.html")
  

def login(req):
  if req.method == "POST":
    username = req.POST["username"]
    password = req.POST["password"]
    user = auth.authenticate(username= username, password= password)

    if user is not None:
      auth.login(req, user)
      return redirect("/gpacalculator")
    else:
      messages.info(req, "invalid credintails")
      return redirect("login")

  else:
    return render(req, "login.html")
  

def logout(req):
  auth.logout(req)
  return redirect("home")


def delete(req):
  if req.method == 'POST':
    marks_id = req.POST['sub_id']
    Marks.objects.filter(id=int(marks_id)).delete()
    return redirect("../")