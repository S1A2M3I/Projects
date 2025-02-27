from django.db import models

class CustomerReview(models.Model):
    text = models.TextField()
    sentiment = models.CharField(
        max_length=10, 
        choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Neutral', 'Neutral')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
