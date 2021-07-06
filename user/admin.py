from django.contrib import admin
from .models import User

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
