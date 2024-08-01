from django.urls import path

from books.views import  IndexView, AboutView, ContactView, ShopView, BookDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='home' ),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]