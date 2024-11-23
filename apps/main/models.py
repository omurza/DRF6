from django.db import models

# Create your models here.
class AughtorModel(models.Model):
    name=models.CharField(max_length=255, verbose_name='имя автора')
    birthay=models.CharField(max_length=100 , verbose_name='дата рождения')

    class Meta:
        verbose_name='автор'
        verbose_name_plural='авторы'

    def __str__(self):
        return self.name
    
class GenreModel(models.Model):
    ganre=models.CharField(max_length=255, verbose_name='жарн')
    
    class Meta:
        verbose_name='жанр'
        verbose_name_plural='жанры'

    def __str__(self):
        return self.ganre
class BookModel(models.Model):

    autor=models.ForeignKey(AughtorModel , null=True , blank=True, on_delete=models.CASCADE)
    genr=models.OneToOneField(GenreModel, on_delete=models.CASCADE)
    year=models.IntegerField(verbose_name='год выпуска')
    title=models.CharField(max_length=255, verbose_name='заголовок')

    
    
    class Meta:
        verbose_name='книга'
        verbose_name_plural='книги'

    def __str__(self):
        return self.title

    book=models.ManyToManyField(BookModel, blank=True)
    ganre=models.CharField(max_length=255, verbose_name='жарн')
    
    class Meta:
        verbose_name='жанр'
        verbose_name_plural='жанры'

    def __str__(self):
        return self.ganre