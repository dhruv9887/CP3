from django.db import models

class video(models.Model):
    name=models.TimeField()
    file=models.FileField(upload_to="Videos")
    image=models.ImageField(upload_to="Videos/thumbnails")
    
    def __str__(self):
        return self.name
    