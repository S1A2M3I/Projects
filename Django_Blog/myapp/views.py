from django.shortcuts import render, redirect
from .models import BlogPost
# Create your views here.

def home(request):
    name = "asdf"
    return render(request, 'myapp/home.html', {"myname":name})

def createpost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f"Title: {title}")
        print(f"Content: {content}")

        if title and content:
            BlogPost.objects.create(title = title, content = content)
            print("Data Saved Successfully")
            return redirect("post_list")
    return render(request, "myapp/createpost.html")



def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'myapp/postlist.html', {'posts': posts})


def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'myapp/postdetail.html', {'post': post})


def update_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)#to fetch the post with the given id

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            post.title = title
            post.content = content
            post.save()
            return redirect('post_list')

    return render(request, 'myapp/updatepost.html', {'post': post})


def delete_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'myapp/deletepost.html', {'post': post})
