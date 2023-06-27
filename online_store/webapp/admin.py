from django.contrib import admin

from webapp.models import Good, Category

admin.site.register(Category)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', "price", 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['category']
    search_fields = ['title', 'description']
    fields = ['title', 'category', 'description', "price", 'image_url', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Good, StoreAdmin)
