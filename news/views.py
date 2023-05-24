from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    ls=Post.objects.all()
    return render(request,'index.html',{'posts':ls})