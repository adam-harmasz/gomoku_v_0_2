from django.contrib import admin

from . import models


admin.site.register(models.Profile)
admin.site.register(models.Player)
admin.site.register(models.GomokuRecord)
admin.site.register(models.GomokuRecordFile)