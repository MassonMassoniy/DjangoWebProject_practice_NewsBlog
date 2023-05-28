from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, User
from .forms import PostForm
from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from news.serializers import PostSerializer, UserSerializer, GetUserSerializer, TokenObtainPairSerializer, TokenRefreshSerializer
from .permissions import *
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

# Create your views here.
def index(request):
    ls = Post.objects.all()
    return render(request, 'index.html', {'news_list':ls})

def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('single', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})

class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['title', 'description', 'text']
    #permission_classes=[IsAuthenticated, IsNewsEditor]

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes=[AllowAny]
        elif self.action in ['create']:
            self.permission_classes=[IsNewsEditor]
        return super(self.__class__, self).get_permissions()
    
class UserView(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=GetUserSerializer
    queryset=User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def get_current_user(self,request,*args,**kwargs):
        serializer=self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenObtainPairSerializer

class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes=[AllowAny]
    serializer_class=TokenRefreshSerializer

class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes=[AllowAny]
    serializer_class=UserSerializer

