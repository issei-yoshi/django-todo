from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=30)
    description = models.TextField(verbose_name="詳細",blank=True)
    deadline = models.DateField(verbose_name="締切日")

    def __str__(self):
        return self.title