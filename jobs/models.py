from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    Summary = models.CharField(max_length=200)
