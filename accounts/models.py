from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models


class Project(models.Model):
    PROJECT_TYPES = [
        ("website", "Veb-sayt"),
        ("webapp", "Web-ilova"),
        ("mobile", "Mobil ilova"),
        ("game", "O‘yin"),
        ("bot", "Telegram bot"),
        ("other", "Boshqa loyiha"),
    ]

    DESIGN_CHOICES = [
        ("cyber", "Cyber neon"),
        ("minimal", "Minimal"),
        ("modern", "Zamonaviy"),
        ("colorful", "Rang-barang"),
    ]

    STATUS_CHOICES = [
        ("draft", "Qoralama"),
        ("progress", "Jarayonda"),
        ("complete", "Tayyor"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    name = models.CharField(max_length=100)
    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES,
        default="website",
    )
    design = models.CharField(
        max_length=20,
        choices=DESIGN_CHOICES,
        default="cyber",
    )
    description = models.TextField(max_length=2000, blank=True)
    features = models.CharField(max_length=500, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

