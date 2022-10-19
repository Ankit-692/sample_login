
from django.db import models

class Messages(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    messages = models.TextField(max_length = 500)
