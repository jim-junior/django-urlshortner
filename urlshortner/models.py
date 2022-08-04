from django.db import models

# Create your models here.


class Url(models.Model):
    url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_permanent = models.BooleanField(default=False)

    def __str__(self):
        return self.url

    def __repr__(self):
        return self.url
