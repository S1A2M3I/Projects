from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"

