from django.db import models

class Document(models.Model):
    POSITION_CHOICES = [
        ('remote', 'Remote'),
        ('offline', 'Offline'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name