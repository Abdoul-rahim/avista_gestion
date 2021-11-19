from django.db import models
from datetime import datetime


class Produit(models.Model):
    code_produit = models.CharField(max_length=20)
    nom_produit = models.CharField(max_length=200)
    prix_unitaire_achat = models.FloatField(default=0)
    prix_unitaire_vente = models.FloatField(default=0)
    quantite = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_produit

class Vente(models.Model):
    id_vente = models.AutoField
    date = models.DateField(default=datetime.now())
    code_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.CharField(max_length=200)
    #TVA = models.Field(default=18)
    quantite_vendue = models.IntegerField(default=1)

class Client(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.IntegerField(max_length=15)
    id_vente = models.ForeignKey(Vente, on_delete=models.CASCADE)

