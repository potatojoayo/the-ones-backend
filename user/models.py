from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, username, password=None):
        if not email:
            raise ValueError('이메일은 필수 입력 사항입니다.')
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, username, password):

        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            username = username,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db) 
        return user 


class User(AbstractBaseUser, PermissionsMixin): 

    objects = UserManager()

    email = models.EmailField(max_length=255, null=False, unique=True) 
    name = models.CharField(max_length=10, null=False)
    username = models.CharField(max_length=10, null=False)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False) 
    like_posts = models.ManyToManyField('post.Post', related_name='likers')
    like_comments = models.ManyToManyField('comment.Comment', related_name='likers')
    favorite_books = models.ManyToManyField('book.Book', related_name='favorings')
    favorite_movies = models.ManyToManyField('movie.Movie', related_name='favorings')

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','username']

    def __str__(self):
        return self.email

