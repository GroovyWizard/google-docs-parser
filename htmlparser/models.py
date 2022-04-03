from django.db import models
from htmlparser.models_helper import validate_file_extension
from htmlparser.models_helper import *

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class RawArchive(TimeStampMixin):
    filename = models.TextField()
    file = models.FileField(upload_to='upload/', validators=[validate_file_extension], null=True, blank=True)
