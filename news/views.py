from django.shortcuts import render
from .models import Post, User
from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from news.serializers import PostSerializer, UserSerializer, GetUserSerializer
from .permissions import *
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    ls = Post.objects.all()
    return render(request, 'index.html', {'posts':ls})

class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['title', 'description', 'text']

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes=[IsAuthenticated, IsNewsEditor]
        else:
            self.permission_classes=[IsAdminUser]
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