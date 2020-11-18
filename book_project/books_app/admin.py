from django.contrib import admin
from books_app import models
# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Publish)