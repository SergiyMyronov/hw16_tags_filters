from bs4 import BeautifulSoup

from django.db import models

import requests


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # supplier rating in range 0..5
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    description = models.TextField(default=' ')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


def get_random_words(num: int):

    word_list = []

    if num > 0:
        r = requests.get('https://random-word-api.herokuapp.com/word?number='+str(num))
        word_list = BeautifulSoup(r.content, features='html.parser')

    return word_list
