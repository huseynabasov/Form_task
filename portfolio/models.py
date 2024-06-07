from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Ad")
    last_name = models.CharField(max_length=30, verbose_name="Soyad")
    father_name = models.CharField(max_length=30, verbose_name="Ata adı")
    age = models.CharField(max_length=3, verbose_name="Yaş")
    city = models.CharField(max_length=30, verbose_name="Şəhər")
    email = models.EmailField(max_length=50, verbose_name="Email")
    job = models.CharField(max_length=30, verbose_name="İş")
    position = models.CharField(max_length=30, verbose_name="Vəzifə")
    biography = models.TextField( verbose_name="Haqqında məlumat")
    skills = models.TextField( verbose_name="Bacarıqları")
    
    def __str__(self):
        return f"{self.job} | {self.first_name} {self.last_name}"