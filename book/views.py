from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from book.models import Book
from book.forms import BookForm, SearchForm


def book_list(request):
    """書籍の一覧"""
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('number')
    return render(request,
                  'book/book_list.html',     # 使用するテンプレート
                  {'books': books})         # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    """書籍の編集"""
    # return HttpResponse('書籍の編集')
    if book_id:   # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:         # book_id が指定されていない (追加時)
        book = Book()

    if request.method == 'POST':
        # POST された request データからフォームを作成
        form = BookForm(request.POST, instance=book)
        if form.is_valid():    # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('book:book_list')
    else:  # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

    return render(
        request,
        'book/book_edit.html',
        dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book:book_list')


def book_search(request):
    """書籍の検索"""
    if request.method == 'POST':
        # POST された request データからフォームを作成
        form = SearchForm(request.POST)
        if form.is_valid():    # フォームのバリデーション

            min_number = request.POST['min_number']
            max_number = request.POST['max_number']
            name_req = request.POST['name']
            author_req = request.POST['author']
            publisher_req = request.POST['publisher']

            if request.POST['min_number'] == '':
                min_number = '0'
            if request.POST['max_number'] == '':
                max_number = '500'

            books = Book.objects.filter(
                name__icontains=name_req,
                author__icontains=author_req,
                publisher__icontains=publisher_req,
                number__gte=min_number,
                number__lte=max_number).order_by("number")

            return render(request,
                          'book/book_search_result.html',     # 使用するテンプレート
                          {'books': books})
    else:    # GET の時
        form = SearchForm(request.GET)  # book インスタンスからフォームを作成
    return render(request, 'book/book_search.html', dict(form=form))
