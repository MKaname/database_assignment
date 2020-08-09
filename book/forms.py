from django.forms import ModelForm, Form, IntegerField
from book.models import Book


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'number',)


class SearchForm(Form):
    """書籍サーチのフォーム"""
    min_number = IntegerField(label='最小', required=False)

    max_number = IntegerField(label='最大', required=False)
