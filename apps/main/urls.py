from rest_framework.routers import DefaultRouter
from .views import BookApi

router=DefaultRouter()
router.register('books', BookApi, basename='book-api')
urlpatterns = [
    
]
urlpatterns+=router.urls
