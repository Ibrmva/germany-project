from django.db import models

class Category(models.Model):
    type = models.CharField(max_length=70, unique=True)
    subgroup = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        return f'{self.subgroup} --> {self.type}' if self.subgroup else self.type

    class Meta:
        ordering = ('type',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'