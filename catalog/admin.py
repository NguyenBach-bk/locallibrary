from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


# Inline for BookInstance
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Show list Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_of_birth",
        "date_of_death",
    )
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]


# Show list Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
    inlines = [BooksInstanceInline]


# Genre register
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


# Show list BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )
