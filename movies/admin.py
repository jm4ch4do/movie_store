from django.contrib import admin
from .models import Book, BookNumber, Character, Author

# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_editable = ['description']
    list_filter = ['is_published']
    search_fields = ['title']

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)


