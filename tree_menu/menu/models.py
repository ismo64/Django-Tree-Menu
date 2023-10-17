from django.db import models
from django.urls import reverse
# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='childs')


    def __str__(self):
        return f'{self.title}'
    

    def get_absolute_url(self):
        return reverse('show_menu', kwargs={'menu_url': self.url, 'parent_url': self.parent.url})


    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title'])
        ]
        unique_together = ('parent', 'title')
    