from django.contrib import admin

from main.models import *


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    max_num = 10
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine, ]


admin.site.register(Category)
