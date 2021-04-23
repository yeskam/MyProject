from django.db import models
from django.urls import reverse

from account.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, primary_key=True, max_length=100)

    def __str__(self):
        return self.name
    #
    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    added_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    added_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(MyUser, related_name='likers', blank=True, symmetrical=False)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        if self.likes.count():
            return self.likes.count()
        else:
            return 0

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
