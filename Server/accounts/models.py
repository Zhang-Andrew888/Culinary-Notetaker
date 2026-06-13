from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    """
    Profile Model that stores the creation and update dates. 
        - one-to-one relation with the User Model.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)