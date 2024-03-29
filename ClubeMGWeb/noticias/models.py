from django.db import models


class Categoria(models.Model):
    designacao = models.CharField("designação", max_length=64)


class Etiqueta(models.Model):
    designacao = models.CharField("designação", max_length=128)


class Noticia(models.Model):
    class Meta:
        get_latest_by = "ultima_actualizacao"
        ordering = ['-destacada', '-id_noticia']
        verbose_name = "notícia"

    id_noticia = models.PositiveIntegerField("identificação da notícia", primary_key=True)
    titulo = models.CharField("título", max_length=256)
    subtitulo = models.CharField("subtítulo", max_length=256)
    texto = models.TextField()
    end_noticia = models.URLField("endereço da notícia")
    end_img = models.URLField("endereço da imagem")
    end_img_grande = models.URLField("endereço da imagem grande")
    imagem = models.ImageField()
    destacada = models.BooleanField(default=False)
    categorias = models.ManyToManyField(to=Categoria)
    etiquetas = models.ManyToManyField(to=Etiqueta)

    ultima_actualizacao = models.DateTimeField("última actualização", auto_now=True, editable=False, blank=True)
