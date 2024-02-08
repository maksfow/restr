from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Kuxnya)
admin.site.register(models.Zavedeniye)
admin.site.register(models.Restaurant)
admin.site.register(models.MenuItem)
admin.site.register(models.Review)
admin.site.register(models.Menu)

