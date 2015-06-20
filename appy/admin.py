from django.contrib import admin
from appy.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}	


admin.site.register(Photo,PhotoAdmin)

# Register your models here.
