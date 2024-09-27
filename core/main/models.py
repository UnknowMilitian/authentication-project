from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(_("Phone Number"), max_length=25, unique=True)
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    bio = models.CharField(_("Bio"), max_length=500, null=True, blank=True)

    # Add related_name for groups and user_permissions to avoid conflict
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_user_set",  # Avoid clash with the default user model
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_user_permissions_set",  # Avoid clash with the default user model
    )

    def __str__(self):
        return self.phone_number


class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_profile",
    )
    location = models.CharField(_("Location"), max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(
        _("Profile Picture"), upload_to="profile-picture"
    )

    def __str__(self):
        return self.user.username
