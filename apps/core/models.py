from django.db import models

class SiteHeader(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='header/')
    location = models.CharField(max_length=100, blank=True)
    availability = models.CharField(max_length=100, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title