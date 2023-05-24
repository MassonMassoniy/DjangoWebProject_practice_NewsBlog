from .models import Post, User
from rest_framework import serializers

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    user_info=serializers.SerializerMethodField()
    
    class Meta:
        model=Post
        fields='__all__'

    def get_user_info(self,obj):
        serializer=GetUserSerializer(obj.user)
        return serializer.data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password',]