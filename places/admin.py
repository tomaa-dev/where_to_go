from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    fields = [('place_image', 'get_preview'), 'position']
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 100%; object-fit: contain;" />',
                obj.place_image.url
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]


admin.site.register(Place, PlaceAdmin)