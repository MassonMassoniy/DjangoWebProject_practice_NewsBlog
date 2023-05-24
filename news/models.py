from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager
from django.contrib.auth.hashers import make_password
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN, NEWS_EDITOR, READER = range(1,4)

    ROLE_TYPES = (
        (ADMIN,'Администратор'),             #1
        (NEWS_EDITOR,'Новостной редактор'),  #2
        (READER,'Читатель')              #3
    )

    objects = UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField('Логин', max_length=50, default='', unique=True)
    first_name = models.CharField("ФИО",max_length=100, default='', blank=True,null=True)
    email = models.EmailField("Почта",default="email@mail.com",blank=True,null=True)
    role = models.IntegerField(verbose_name='Роль',default=READER,choices=ROLE_TYPES)
    date_joined = models.DateTimeField("Дата присоединения",blank=True,null=True,default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус доступа',
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Post(models.Model):
    
    DAILY_NEWS, IMPORTANT_NEWS, INTERESTING_NEWS, JUST_NEWS = range(1,5)

    NEWS_TYPES = (
        (DAILY_NEWS, 'Новость дня'),
        (IMPORTANT_NEWS, 'Срочные новости'),
        (INTERESTING_NEWS, 'Интересные новости'),
        (JUST_NEWS, 'Обычные новости'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Пользователь создавший новость', null=True,blank=True, related_name='news')
    title = models.CharField(verbose_name='Заголовок новости',max_length=255,default='',null=True,blank=True)
    text = models.TextField(verbose_name='Описание новости')
    description = models.TextField(verbose_name='Текст новости')
    news_type = models.IntegerField(verbose_name='Тип новости',default=JUST_NEWS,choices=NEWS_TYPES)
    date_post = models.DateTimeField(default=timezone.now,verbose_name='Дата создания новости')

    

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'

    def __str__(self) -> str:
        return self.title