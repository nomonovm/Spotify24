from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=222)
    t_sana = models.DateField()
    davlat = models.CharField( max_length=222)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = "Qo'shiqchilar"

class Albom(models.Model):
    nom = models.CharField(max_length=222)
    sana = models.DateField()
    rasm = models.ImageField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Albomlar'

class Qoshiq(models.Model):
    nom = models.CharField(max_length=111)
    janr = models.CharField(max_length=111)
    davomiylik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "Qo'shiqlar"