from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    """
    Profile Model that has firebase uid, name, creation date, and recently updated date. This model is tied to the Django User Model with a one-to-one relation.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    # firebase_uid = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=150, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.name}"