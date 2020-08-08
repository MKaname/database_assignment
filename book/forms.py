from django.forms import ModelForm, Form, IntegerField
from book.models import Book


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page',)


class SearchForm(Form):
    """書籍サーチのフォーム"""
    min_page = IntegerField(label='最小ページ数', required=False)

    max_page = IntegerField(label='最大ページ数', required=False)
