from django.contrib import admin
from book.models import Book, Impression

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'number',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)  # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）


admin.site.register(Impression)
