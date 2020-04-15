from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from . models import User
# Register your models here.
User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
