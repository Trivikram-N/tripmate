from django.contrib import admin
from .models import Place, Category, Attraction

admin.site.register(Place)
admin.site.register(Category)

class AttractionAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_place_title')

    def get_place_title(self, obj):
        return obj.place.title
    get_place_title.short_description = 'Place'

admin.site.register(Attraction, AttractionAdmin)