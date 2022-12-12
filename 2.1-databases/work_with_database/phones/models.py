from django.db import models


class Phone(models.Model):
    name = models.CharField(u'Наименование', max_length=120)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.IntegerField(u'Стоимость')
    image = models.CharField(u'Фотография', max_length=200)
    release_date = models.DateField(u'Дата публикации')
    lte_exists = models.BooleanField(u'Наличие')

    prepopulated_fields = {"slug": ("name", )}

    def __str__(self):
        return self.name
