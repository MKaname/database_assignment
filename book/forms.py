from django.forms import ModelForm, Form, IntegerField, CharField
from book.models import Book


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'number',)


class SearchForm(Form):
    """書籍サーチのフォーム"""
    name = CharField(label = '作品名', required=False)
    author = CharField(label = '作者', required=False)
    publisher = CharField(label = 'レーベル', required = False)

    min_number = IntegerField(label='最小巻数', required=False)
    max_number = IntegerField(label='最大巻数', required=False)


