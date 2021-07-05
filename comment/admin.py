from django.contrib import admin
from .models.comment import Comment
from .models.comment_of import Comment_Of

# Register your models here.

admin.site.register(Comment)
admin.site.register(Comment_Of)
