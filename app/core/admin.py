from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Board)
admin.site.register(models.Task)
admin.site.register(models.Group)

