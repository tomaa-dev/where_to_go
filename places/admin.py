from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    fields = [('image', 'get_preview'), 'position']
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 100%; object-fit: contain;" />',
                obj.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]