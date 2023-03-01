from django.db import models


# класс для главной страницы
# class Mainindex(models.Model):
#     title = models.CharField('Название', max_length=50)
#
#     class Meta:
#         verbose_name = 'Главная'
#         verbose_name_plural = 'Главная страница'


# класс выбора меню
class RegisterMenu(models.Model):
    LABELS = {
        'name': 'Name',
        'verbose_name': 'Verbose name'
    }

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    name = models.CharField(LABELS['name'], max_length=255, blank=True, null=False)
    verbose_name = models.CharField(LABELS['verbose_name'], max_length=255, blank=True, null=False)

    def __str__(self):
        return self.verbose_name


# класс подменю
class MenuTree(models.Model):
    LABELS = {
        'name': 'Name',
        'category': 'Category',
        'path': 'Path',
        'parent': 'Parent element',
    }

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    name = models.CharField(LABELS['name'], max_length=255, blank=True, null=False)

    category = models.ForeignKey(
        RegisterMenu,
        verbose_name=LABELS['category'],
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    path = models.SlugField(LABELS['path'], max_length=1000, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=LABELS['parent'],
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name





