from django.contrib import admin
from .models import Post, User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('user', 'title', 'description', 'text', 'date_post')
    list_filter=('user','date_post')
    #fields=[('user', 'title', 'date_post'), 'text', 'description']
    fieldsets=(
        ('Основная информация',{'fields':('user', 'title', 'date_post')}),
        ('Содержание',{'fields':('description', 'text')})
    )

class PostInLine(admin.TabularInline):
    model = Post
    fk_name = 'user'

@admin.register(User)    
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'first_name', 'email', 'role', 'date_joined', 'is_staff', 'is_active')
    list_filter=('role', 'date_joined', 'is_staff', 'is_active')
    fieldsets=(
        ('Основная информация',{'fields':('username', 'first_name', 'email', 'role')}),
        ('Дополнительная информация',{'fields':('date_joined', 'is_staff', 'is_active')})
    )
    inlines = [PostInLine]

# Register your models here

#admin.site.register(Post, PostAdmin)
#admin.site.register(User, UserAdmin)