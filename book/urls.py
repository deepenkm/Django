from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_list, name='book_list'),
    path('book/<str:pk>/detail/',views.book_detail, name='book_detail'),
    path('book/<str:pk>/update/',views.update_book,name='update_book'),
    path('book/create/',views.create_book,name='create_book'),
    path('book/<str:pk>/delete/',views.delete_book,name='delete_book'),

]