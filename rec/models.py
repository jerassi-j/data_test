from django.db import models

# Create your models here.

class item(models.Model):
    itemid = models.BigIntegerField(primary_key=True)
    title = models.TextField(max_length=2000)
    genres = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class rating(models.Model):
    r_id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    itemid = models.BigIntegerField()
    rating = models.FloatField()
    timestamp = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.r_id)