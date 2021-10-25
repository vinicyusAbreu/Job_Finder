from djmoney.models.fields import MoneyField
from django.db import models
from moneyed.classes import BRL
from PIL import Image
from django.conf import settings
import os

# Create your models here.


class Emprego(models.Model):
    titulo_vaga = models.CharField(max_length=255, verbose_name='Título')
    descricao_vaga = models.TextField(verbose_name='Descrição da Vaga')
    empresa_contratante = models.CharField(
        max_length=255, verbose_name='Empresa contratante')
    email_contato = models.EmailField(verbose_name="E-mail para contato")
    salario = MoneyField(max_digits=10, decimal_places=2, default_currency=BRL)
    imagem_empresa = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True,
                                       null=True, verbose_name='Imagem Empresa')

    def __str__(self):
        return self.titulo_vaga

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem_empresa:
            self.resize_image(self.imagem_empresa.name, 512)

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60
        )
        new_img.close()
