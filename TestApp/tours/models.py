from django.db import models

class Tours(models.Model):
    name = models.CharField('Атауы',max_length=60)
    date = models.CharField('Тур уақыты',max_length=250)
    equipment = models.CharField('Номер типі',max_length=20)
    price = models.IntegerField('Тур бағасы')
    img = models.CharField('Фото енгізіңіз',max_length=450)
    category_id = models.IntegerField()


    def __str__(self):
        return f'Тур атауы: {self.name}'


    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Турлар'
