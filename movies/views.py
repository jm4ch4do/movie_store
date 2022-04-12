from rest_framework import viewsets
from .serializers import BookSerializer, BookMiniSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)

    # We are using the default methods for the view
    # But we can also define
    # `create()`, `retrieve()`, `update()`,
    # `partial_update()`, `destroy()` and `list()`
    # To define our own responses to each request
