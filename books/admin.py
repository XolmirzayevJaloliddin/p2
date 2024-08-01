from django.contrib import admin
from books.models import *
# Register your models here.

@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "date_published"
    list_display = ['title', 'date_published', 'price', 'description']
    # fields = ['title', 'price', 'description']


admin.register(Author)
admin.site.register(Genre)
