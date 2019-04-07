from django.db import models
from uuid import uuid5

# Create your models here.

class Contact(models.Model):
    id = models.UUIDField(default=uuid5, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='attachments/')