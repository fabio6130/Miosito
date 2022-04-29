from django.db import models

# Create your models here.


class Interesse(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Abilita(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Passione(models.Model):
    name=models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name



class ProgettiFatti(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
