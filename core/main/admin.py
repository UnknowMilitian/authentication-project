from django.contrib import admin
from .models import User, UserProfile, Action, ActionLog, Item


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
