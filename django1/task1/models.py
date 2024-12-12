from django.db import models

class Buyer(models.Model):

    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name




