from django.contrib import admin

from .models import Author, Book, BookInstance, Genre
from .admins.book_admin import BookAdmin
from .admins.author_admin import AuthorAdmin
from .admins.book_instance_admin import BookInstanceAdmin
from .admins.genre_admin import GenreAdmin


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre, GenreAdmin)
