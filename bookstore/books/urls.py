# books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BookDetailAPIView

# For ViewSet approach
# router = DefaultRouter()
# router.register('books', BookViewSet)

urlpatterns = [
    # APIView routes
    path('api/manual/books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/manual/books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    # ModelViewSet routes
    # path('api/viewset/', include(router.urls)),
]
