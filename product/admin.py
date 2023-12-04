from django.contrib import admin
from . import models


class Information_1Admin(admin.StackedInline):
    model = models.Information_1

class AttributMainAdmin(admin.StackedInline):
    model = models.AttributeMain


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "created")
    inlines = (Information_1Admin,AttributMainAdmin)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "parent")
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Size)
admin.site.register(models.Color)
admin.site.register(models.AttributDetail)