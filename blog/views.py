from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post

# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def writeBlog(request):
    if request.method == "POST":
        Title = request.POST['Title']
        Author = request.POST['Author']
        Content = request.POST['Content']
        if len(Title) < 2 or len(Author) < 3 or len(Content) < 10:
            messages.error(request, "Please fill the boxes correctly")
        else:
            writeBlogData = Post(title=Title, author=Author, content=Content)
            writeBlogData.save()
            messages.success(
                request, "Your blog has been successfully posted")
    return render(request, "blog/writeBlog.html")

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")

def author(request):
    return render(request,"blog/author.html")