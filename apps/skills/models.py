from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    category = models.CharField(max_length=100)

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="intermediate")
    def __str__(self):
        return self.name