# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, UserProfile, Action, ActionLog


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create User Profile
        UserProfile.objects.create(user=instance)

        # Log Action for User Creation
        action = Action.objects.get_or_create(title="User Created")[0]
        ActionLog.objects.create(user=instance, action=action)


@receiver(post_save, sender=UserProfile)
def log_user_profile(sender, instance, created, **kwargs):
    # Determine action title based on whether profile was created or updated
    action_title = "Profile Created" if created else "Profile Updated"

    # Log Action for Profile
    action = Action.objects.get_or_create(title=action_title)[0]
    ActionLog.objects.create(user=instance.user, action=action)


@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    # Log Action for User Deletion
    action = Action.objects.get_or_create(title="User Deleted")[0]
    ActionLog.objects.create(user=instance, action=action)
