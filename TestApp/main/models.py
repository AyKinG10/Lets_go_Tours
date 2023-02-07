from django.db import models

class Category(models.Model):
    name = models.CharField('Категория атауы', max_length=23)
    def __str__(self):
        return self.name