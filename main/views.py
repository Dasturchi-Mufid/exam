from django.shortcuts import render
from . import models

def index(request):
    destinations = models.Destination.objects.all()
    posts = models.Post.objects.all()
    socials = models.Social.objects.all()
    abouts = models.AboutUs.objects.all()
    context = {
        'destinations':destinations,
        'posts':posts,
        'abouts':abouts,
        'socials':socials,
    }
    return render(request,'index.html', context=context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def destination(request):
    return render(request,'destination.html')

def hotel(request):
    return render(request,'hotel.html')

def blog(request):
    posts = models.Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'blog.html',context)

def blog_detail(request,id):
    post = models.Post.objects.get(id=id)
    recent_posts = models.Post.objects.all()[::-1]
    context = {
        'post':post,
        'recent_posts':recent_posts,}
    return render(request,'detail.html',context)