from django.db import models

# Create your models here.
class Project(models.model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to="project")


    def __str__(self):
        return self.title
    