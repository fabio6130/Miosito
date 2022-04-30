from django.db import models

# Create your models here.


class Companies(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image=models.ImageField(upload_to='image')
    url=models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Projects(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image=models.ImageField(upload_to='image')
    url=models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Languages(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    frontend = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class DevTools(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    frontend = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name