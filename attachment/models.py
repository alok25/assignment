from django.db import models

from user_auth.models import User


class AssetsManagement(models.Model):
    """
    Base class to stores attachments
    """

    name = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to='assets', blank=True,
                                  null=True)
    created_by = models.ForeignKey(User, related_name="assets_created_user")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'assets_management'
