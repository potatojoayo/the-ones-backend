from django.contrib import admin
from .models.user import User
from .models.follow import Follow
from .models.like_post import Like_Post
from .models.like_comment import Like_Comment

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'username',
        'birthday',
        'gender',
        'date_joined',
    )

    list_display_links = (
        'email',
        'username',
        'name'
    )

admin.site.register(Follow)
admin.site.register(Like_Comment)
admin.site.register(Like_Post)
