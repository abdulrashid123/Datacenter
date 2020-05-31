from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Table(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('table:detail', kwargs={'pk': self.pk})


class Parameter(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    parameter_title = models.CharField(max_length=250)
    unit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        ordering = ('parameter_title',)

    def __str__(self):
        return self.parameter_title


class Values(models.Model):
    parameter = models.ForeignKey(Parameter,default=1, on_delete=models.CASCADE)

    datetime = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

