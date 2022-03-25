from blog.views import Blogpost
from django import http
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.api import error
from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.core.mail import message, send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, subject, message)
        if len(name) < 2 or len(email) < 3 or len(message) < 4:
            messages.error(request, "Please fill your form correctly")
        else:
            contact = Contact(name=name, email=email, content=message)
            contact.save()
            messages.success(request, "Your message was delivered Succesfully")
    return render(request, 'contact.html')


def about(request):
    # return(HttpResponse("This is about page"))
    return render(request, 'about.html')


def followMe(request):
    return render(request, 'social.html')


def search(request):

    query = request.GET["query"]
    if len(query) > 30:
        posts = Post.objects.none()
    else:
        postsTitle = Post.objects.filter(title__icontains=query)
        postsContent = Post.objects.filter(content__icontains=query)
        posts = postsTitle.union(postsContent)

    if len(query) == 0:
        messages.warning(request, "Are you trying to search something, if 'yes' then refine your query")
        Post.objects.none()
        return render(request, 'search.html')
   
    else:    
        params = {"posts": posts, "query": query}
        return render(request, "search.html", params)


def handeleSignup(request):
    if request.method == "POST":
        """Get the user details"""
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        """check for errorneous inputs"""
        if len(username) > 10:
            messages.error(request,
                           "Your username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(
                request,
                "Username should only conatain only letters and numbers")
            return redirect('home')
        if password1 != password2:
            messages.error(request, "Both the passwords must be same")
            return redirect('home')
        if len(password1) < 8:
            messages.error("Password needs to be atleast <b>8<b/> characters long\n")
        """creating user"""
        myuser = User.objects.create_user(username=username,
                                          email=email,
                                          password=password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        return redirect('home')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


# login function
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['lusername']
        password = request.POST['lpassword']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in succesfully\n")
            return redirect("home")
        else:
            messages.error(request,"You are not authorized, Check your credentials\n")
            return redirect('home')
    return HttpResponse("<h1>404 - Not Found</h1>")
    

# logout function
def handleLogout(request):
    logout(request)
    messages.success(request, "You are succesfully logged out")
    return redirect('home')

