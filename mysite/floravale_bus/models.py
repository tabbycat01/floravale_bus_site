from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=50)
    feedback = models.TextField()

    def __str__(self):
        return self.description