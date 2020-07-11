from django.contrib import admin
from Jiawem import models 

myModels = [
    models.Person,
    models.Pastor,
    models.Singer,
    models.Band,
    models.Usher,
    models.Deacon,
    models.PrayerRequest
    ]
# Register your models here.
admin.site.register(myModels)