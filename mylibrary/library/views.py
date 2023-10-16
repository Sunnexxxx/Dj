from django.shortcuts import render
from .models import Book, Reader, BookRent


# Create your views here.
def show_start_page(request):
    return render(request, "index.html")


def show_showbooks_page(request):
    context = {"books": Book.objects.all()}

    return render(request, "showBooks.html", context=context)


def show_addbook_page(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("book_author_surname")
        genre = request.POST.get("book_genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count") if request.POST.get("page_count") else 0
        description = request.POST.get("description")

        Book.objects.create(title=book_title,
                            author_name=author_name,
                            author_surname=author_surname,
                            genre=genre,
                            publication_year=publication_year,
                            page_count=page_count,
                            description=description)

    return render(request, "addBook.html")


def show_addreader_page(request):
    if request.method == "POST":
        name = request.GET.get("reader_name")
        surname = request.POST.get("reader_surname")
        age = request.POST.get("reader_age")
        address = request.GET.get("reader_address")

        Reader.objects.get(name=name,
                           surname=surname,
                           age=age,
                           address=address)

    return render(request, "addReader")


def show_addrent_page(request):
    if request.METHOD == "POST":
        title = request.POST.get("book_title")
        reader = request.POST.get("reader_surname")
        rent_date = request.POST.get("rent_date")
        return_date = request.POST.get("return_date")

        BookRent.objects.delete(book_title=title,
                                reader_surname=reader,
                                rent_date=rent_date,
                                return_date=return_date)

    return render(request, "add_Rent.html")

