from django.db import models

class rpgclass(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=700)
    life = models.IntegerField(max_length=5)
    main_skill = models.CharField(max_length=20)
    strength = models.IntegerField(max_length=2)
    des = models.IntegerField(max_length=2)
    con = models.IntegerField(max_length=2)
    int = models.IntegerField(max_length=2)
    wisdom = models.IntegerField(max_length=2)
    charism = models.IntegerField(max_length=2)
