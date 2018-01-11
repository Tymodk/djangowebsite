from django.db import models

# Create your models here.
class Richting(models.Model):
    naam = models.CharField(max_length=100)
    omschrijving = models.CharField(max_length=500)
    def __str__(self):
        return "%s" % (self.naam)

class Leraar(models.Model):
    voornaam = models.CharField(max_length=100)
    naam = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='images')
    email = models.CharField(max_length=300)
    def __str__(self):
        return "%s %s" % (self.voornaam, self.naam)

class Klas(models.Model):
    naam = models.CharField(max_length=100)
    numerieke_code = models.IntegerField()
    richting = models.ForeignKey(Richting, on_delete=models.CASCADE)
    leraar = models.ForeignKey(Leraar, on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % (self.naam)

class Contact(models.Model):
    email = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    telenummer = models.CharField(max_length=100)
    inhoud = models.CharField(max_length=5000)
    def __str__(self):
        return "Bericht van %s" % (self.email)
