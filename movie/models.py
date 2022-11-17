from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    descriptiom = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/', height_field=None, width_field=None, max_length=100)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title
