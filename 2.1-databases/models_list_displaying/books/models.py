# coding=utf-8

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name + " " + self.author

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.pub_date)
        return super().save(*args, **kwargs)
