from django.db import models
from django.db.models.deletion import CASCADE


class Manga(models.Model):
    manga_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)  # seo max characters
    author = models.CharField(max_length=38)
    thumbnail = models.URLField()
    thumbnail_id = models.IntegerField(default=-1)
    brief = models.TextField()
    rating = models.FloatField()
    date = models.DateField(null=True)
    tags = models.ManyToManyField("Tag")


class Picture(models.Model):
    pic_id = models.AutoField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=38, unique=True)
    description = models.TextField()
    owner = models.CharField(max_length=38)
    mangas = models.ManyToManyField(Manga)


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)

