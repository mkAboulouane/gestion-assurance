from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    nom=models.CharField(max_length=200)
    cne=models.CharField(max_length=50)
    date_naissance=models.DateTimeField()
    telephone=models.CharField(max_length=30)
    Matricule=models.CharField(max_length=100)
    type_contrat=models.CharField(max_length=50)
    num_contrat=models.IntegerField(default=1)
    date_start=models.DateTimeField()
    date_end=models.DateTimeField()
    type_vehicule=models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.cne)
    class Meta:
        ordering = ['-updated','-created']
    
    