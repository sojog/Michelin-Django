from django.db import models

# Create your models here.


class PasswordModel(models.Model):
    content = models.CharField(max_length=15)

    def __str__(self):
        return self.content
