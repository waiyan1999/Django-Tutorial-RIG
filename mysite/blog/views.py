from django.shortcuts import render
from blog.models import Post
from blog.models import myfriends

# Create your views here.

def postdata(request): #come fromm contorller 
    post_data = Post.objects.all()
    context = {'post_data': post_data}
    return render(request,'posts.html',context)

def myfriend(request):
    data = myfriends.objects.all()
    context = {'data':data}
    return render(request,'myfirend.html',context)