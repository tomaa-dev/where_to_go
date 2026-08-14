from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    fields = [('place_image', 'get_preview'), 'position']
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 100%; object-fit: contain;" />',
                obj.place_image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]