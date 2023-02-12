from django.contrib import admin

from service_app.models import Valentine, User


@admin.register(Valentine)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "status")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)
