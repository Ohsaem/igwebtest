from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from . import models

# Create your views here.
def create(request):
    return render(request, 'create.html')

def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        title = request.POST['title']
        body = request.POST['body']
        file = request.FILES.get('file')
        post = models.Post(
            title = title,
            body = body,
            file = file
        )
        post.save()

    post = models.Post.objects.all()
    
    return redirect('main')