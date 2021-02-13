from django.contrib import admin

from todo.core.models import Todo, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('id',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'description',
        'date',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id',)
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'category__id')
