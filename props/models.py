# -*- coding: latin-1 -*-


from django.db import models


class Prop(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    price = models.CharField(max_length=20, null=True, blank=True, verbose_name='Precio (opcional)')
    location = models.CharField(max_length=100, verbose_name='Ubicacion')
    desc = models.TextField(verbose_name='Descripcion')

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        return "{}".format(self.title)


class PropImage(models.Model):
    prop = models.ForeignKey(Prop, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='propiedades', verbose_name='Imagen')

    def __str__(self):
        return '{}'.format(self.image)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'


