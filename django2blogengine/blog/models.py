from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts') # создает поле у двух таблиц (манипуляция через менеджер объектов)
    data_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_url_create(self):
        return reverse("post_create")

    def get_url_delete(self):
        return reverse("post_delete", kwargs={'slug':self.slug})

    def get_url_update(self):
        return reverse("post_update", kwargs={'slug':self.slug})
    

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
    
    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})


    def get_url_create(self):
        return reverse("tag_create")

    def get_url_delete(self):
        return reverse("tag_delete", kwargs={'slug':self.slug})

    def get_url_update(self):
        return reverse("tag_update", kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)
