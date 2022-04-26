from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,login,logout
from blog.models import Post

def index(request): 
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return redirect('/login/')

def home(request): 
    if request.user.is_authenticated:
        allPosts = Post.objects.all().order_by('-timeStamp')
        context={'allPosts': allPosts}
        return render(request, "home/home.html",context)
    else:
        return redirect('/login/')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<3:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, Message=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def search(request):
    if request.user.is_authenticated:
        query=request.GET['query']
        if len(query)>78:
            allPosts=Post.objects.none()
        else:
            allPostsTitle= Post.objects.filter(title__icontains=query)
            allPostsAuthor= Post.objects.filter(author__icontains=query)
            allPostsContent =Post.objects.filter(content__icontains=query)
            allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor,allPostsTitle)
            profile=''
            try:
                profile = User.objects.get(username=query)
            except:
                print(f'User {query} not found')
        if allPosts.count()==0:
            messages.warning(request, "No search results found. Please refine your query.")
        else:
            context={
                'allPosts': allPosts,
                'query': query,
                'profile': profile,
            }
            return render(request, 'home/search.html', context)
    else:
        return redirect('/login/')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # profilePic=request.POST['profilePic']
        profilePic = request.FILES.get("profilePic")

        # check for errorneous input
        if len(username)>15:
            messages.error(request, " Your user name must be under 15 characters")
            return redirect('/signup/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/signup/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/signup/')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        userprofilePic = ProfilePic(profilePic=profilePic)
        userprofilePic.save()
        messages.success(request, "Your account has been successfully created")
        user=authenticate(username= username, password= pass1)
        if user is not None:
            login(request, user)
            return redirect("/home/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login/")

    else:
        return render(request,'home/signup.html')

def handeLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome Back @{user}")
            return redirect("/home/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login/")

    return render(request,"home/login.html")

def handelLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('/login/')
    else:
        return redirect('/login/')

def profile(request):
    if request.user.is_authenticated:
        # post=Post.objects.filter(slug=slug).first()
        allUsers=User.objects.all()
        allUsersObj={
            'allUsers':allUsers
        }
        return render(request,"home/profile.html",allUsersObj)
    else:
        return redirect('/login/')

def confirmdeleteaccount(request):
    if request.user.is_authenticated:
        # username = request.user
        # User.objects.filter(username=username).delete()
        return render(request,'home/confirmdeleteaccount.html')
    else:
        return redirect('/login/')

def deleteaccount(request):
    if request.user.is_authenticated:
        username = request.user
        User.objects.filter(username=username).delete()
        return HttpResponse(f'<h2>{username} your account has deleted</h2>')
    else:
        return redirect('/login/')

def username(request,username):
    if request.user.is_authenticated:
        user = User.objects.filter(username=username).first()
        user_slugObj={'user_slug':user}
        return render(request,'home/user.html',user_slugObj)
    else:
        return redirect('/login/')

def changepassword(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # Get the post parameters
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            if (oldpassword!= newpassword):
                messages.error(request, " Passwords do not match")
            else:
                user = User.objects.filter(username=request.user).first()
                user.set_password(newpassword)
                user.save()
            return redirect('/profile/')
    else:
        return redirect('/login/')

def addtodo(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            todotitle=request.POST['todotitle']
            todoDescription=request.POST['todoDescription']
            return redirect('/profile/')
    else:
        return redirect('/login/')

# obj = get_object_or_404(modelname, name=name)
# obj.delete()
# request.user.get_username()