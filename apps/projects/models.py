from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/')
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(max_length=100, default="Mobile")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title