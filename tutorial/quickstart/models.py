from django.db import models

class DocumentRecord(models.Model):
    """
    Model for saving Documents
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    document_type = models.CharField(max_length=255, blank=True, null=True)
    document_location = models.CharField(max_length=255, blank=True, null=True)
    document_url = models.URLField(null=True)
    storage = models.CharField(max_length=125)
    name = models.CharField(max_length=125, null=True)
