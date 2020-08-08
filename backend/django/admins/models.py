from django.db import models

# Create your models here.
class PolicyCreation(models.Model):
    policyname= models.CharField(max_length=100)
    description= models.TextField()
    def __str__(self):
        return self.policyname