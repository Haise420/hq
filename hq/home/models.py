from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=45, blank=True, null=True)
    slika = models.ImageField(upload_to='slike_clanova/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Beleska(models.Model):
    naslov = models.CharField(max_length=26, blank=True, null=True)
    text = models.TextField(max_length=6000)
    kreiran = models.DateTimeField(auto_now_add=True)



class Projekat(models.Model):
    ime = models.CharField(max_length=18)
    deskripcija = models.TextField(max_length=6000)
    aktivnost = models.ForeignKey(Clan, related_name='aktivnosti', on_delete=models.SET_NULL, null=True, blank=True)
    clanovi = models.ManyToManyField(Clan)

    slika = models.ImageField(upload_to='slike_projekta/', null=True, blank=True)

    def __str__(self):
        return self.ime
    
class Masina(models.Model):
    ip_adresa = models.CharField(max_length=20)
    ssh_username = models.CharField(max_length=20)
    ssh_password = models.CharField(max_length=25)
    ssh_port = models.IntegerField()
    ime = models.CharField(max_length=18)
    sistem_instaliran = models.TextField()
    kreiran = models.DateTimeField(auto_now_add=True)
    pristup = models.ManyToManyField(Clan)
    istice = models.DateField()
    aktivna = models.BooleanField()

