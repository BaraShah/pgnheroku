from django.db import models

# Create your models here.

class pgn(models.Model):
    name = models.CharField(max_length=30)
    ringnum = models.IntegerField(null=True, blank=True)
    egg = models.CharField(max_length=5)
    eggnum = models.CharField(max_length=2)
    eggday = models.DateField(null=True, blank=True)
    childay = models.DateField(null=True, blank=True)
    homenum = models.IntegerField(null=True, blank=True)
    roomnum = models.IntegerField(null=True, blank=True)
    nurseringnum = models.IntegerField(null=True, blank=True)

    def __str__ (self):
        return self.name

    class Meta:
        ordering = ['name', 'ringnum' , 'egg' , 'eggnum']
