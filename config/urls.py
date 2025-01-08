from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import CategoryViewSet, BookViewSet, BookLoanViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'loans', BookLoanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
