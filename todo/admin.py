from typing import Sequence
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created',)

admin.site.register(Todo, TodoAdmin)