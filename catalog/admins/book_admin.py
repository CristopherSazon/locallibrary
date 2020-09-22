from django.contrib import admin

from catalog.models import BookInstance


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
