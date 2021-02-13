from django.db import models


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractModel):
    name = models.CharField(verbose_name='Categoria', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.name


class Todo(AbstractModel):
    category = models.ForeignKey(
        'core.Category', verbose_name='Categoria', related_name='todo', on_delete=models.DO_NOTHING
    )
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.TextField(verbose_name='Descrição', default='')
    date = models.DateField(verbose_name='Data', blank=True, null=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ('date',)

    def __str__(self) -> str:
        return self.name
