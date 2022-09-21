from pyexpat import model
from django.db import models
from django.conf import settings
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True, null=True)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('viewtodo', args=(self.pk, ))

    def __str__(self) -> str:
        return self.title 