from django.db import models


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=150)
    image_class = models.CharField(max_length=50)
    image_percentaje = models.FloatField()
