from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ModelBase(models.Model):
    is_published = models.BooleanField('Опубликовано',
                                       default=True,
                                       help_text='''Снимите галочку,
                                       чтобы скрыть публикацию.''')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class Category(ModelBase):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True,
                            help_text='''Идентификатор страницы для URL;
                            разрешены символы латиницы, цифры, дефис
                            и подчёркивание.''')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(ModelBase):
    name = models.CharField('Название места', max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(ModelBase):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateField('Дата и время публикации',
                                help_text='''Если установить дату и время в 
                                будущем —
                                можно делать отложенные публикации.''')
    author = models.ForeignKey('Автор публикации', 
                               User, on_delete=models.CASCADE)
    location = models.ForeignKey('Местоположение', Location,
                                 on_delete=models.SET_NULL,
                                 null=True)
    category = models.ForeignKey('Категория', Category,
                                 on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
