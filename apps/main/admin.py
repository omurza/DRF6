from django.contrib import admin
from .models import BookModel, AughtorModel, GenreModel

# Админка для модели AughtorModel
@admin.register(AughtorModel)
class AdminAughtor(admin.ModelAdmin):
    fields = ['name', 'birthay']
    list_display = ['name', 'birthay']

# Админка для модели BookModel
@admin.register(BookModel)
class AdminBook(admin.ModelAdmin):
    fields = ['autor', 'title', 'year']
    list_display = ['autor', 'title', 'year']

    # Если 'autor' - это внешний ключ или связь многие ко многим, используйте метод
    def autor_name(self, obj):
        return obj.autor.name  # Если 'autor' — это внешний ключ на модель AughtorModel
    autor_name.short_description = 'Автор'
    
    list_display = ['autor_name', 'title', 'year']

# Админка для модели GenreModel
@admin.register(GenreModel)
class AdminGenre(admin.ModelAdmin):
    fields = ['book', 'ganre']
    list_display = ['book', 'ganre']

    # Если 'book' — это связь многие ко многим, используйте метод для отображения
    def book_titles(self, obj):
        return ", ".join([book.title for book in obj.book.all()])
    book_titles.short_description = 'Книги'

    list_display = ['book_titles', 'ganre']
