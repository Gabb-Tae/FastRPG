from django.db import models

class rpgclass(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=700)
    life = models.IntegerField(max_length=5)
    main_skill = models.CharField(max_length=20)
    strength = models.IntegerField(max_length=2)
    dexterity = models.IntegerField(max_length=2)
    constitution = models.IntegerField(max_length=2)
    intelligence = models.IntegerField(max_length=2)
    wisdom = models.IntegerField(max_length=2)
    charism = models.IntegerField(max_length=2)

class skills(models.Model):
    description = models.CharField(max_length=1000)

class itens(models.Model):
    description = models.CharField(max_length=100)
    damage = models.CharField(max_length=50)

class rpgrace(models.Model):
    name = models.CharField(max_length=50)
    features = models.CharField(max_length=700)
    life = models.IntegerField(max_length=5)
    size = models.CharField(max_length=20)
    speed = models.CharField(max_length=20)
    languages = models.CharField(max_length=60)
    strength = models.IntegerField(max_length=2)
    dexterity = models.IntegerField(max_length=2)
    constitution = models.IntegerField(max_length=2)
    intelligence = models.IntegerField(max_length=2)
    wisdom = models.IntegerField(max_length=2)
    charism = models.IntegerField(max_length=2)

