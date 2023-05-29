from django.contrib import admin
from .models import Post, User

class PostAdmin(admin.ModelAdmin):
    list_display=('user', 'title', 'description', 'text', 'date_post')
    list_filter=('user','date_post')

# Register your models here
admin.site.register(Post, PostAdmin)
admin.site.register(User)