from django.shortcuts import render, redirect,get_object_or_404
from .models import Book
from django.http import Http404
# Create your views here.
def book_list(request):
    books = Book.objects.all()

    return render(request ,'book_list.html',{'books':books})

def book_detail(request,pk):

    #book = Book.objects.get(id=pk)
    book = get_object_or_404(Book, id=pk)

    return render(request,'book_detail.html',{'book':book})


def create_book(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description')
        book = Book.objects.create(title=title, author=author, price=price, description=description)
        book.save()
        return redirect('book_list')
    else:
        return render(request,'create_book.html')

def update_book(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description')
        book.title=title
        book.author=author
        book.price=price
        book.description= description
        book.save()
        return redirect('book_list')
    else:
        return render(request,'update_book.html',{'book':book})

def delete_book(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book_list')
