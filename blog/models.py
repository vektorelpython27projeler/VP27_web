from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    # yazar
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
    baslik = models.CharField(max_length=100,verbose_name="Başlık")
    yazi = models.TextField(verbose_name="Yazı")
    secenekler = [("1","Korku"),("2","Gezi"),("3","Hayata Dair")]
    tur = models.CharField(choices=secenekler,max_length=10,verbose_name="Tür")
    kayitzaman = models.DateTimeField(default=timezone.now,verbose_name="Kayıt Zamanı")
    yayimzaman = models.DateTimeField(null=True,blank=True,verbose_name="Yayımlanma Zamanı")

    def yayimla(self):
        self.yayimzaman = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik

