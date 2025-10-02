from django.db import models
from django.urls import reverse


class GeneratedImage(models.Model):
    prompt = models.TextField()
    image = models.ImageField(upload_to='generated/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.prompt[:50]

    def get_absolute_url(self):
        return reverse('generator:image_detail', args=[self.id])