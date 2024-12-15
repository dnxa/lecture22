from django.urls import path
from .views import get_product_view, delete_product_view, create_product_view

urlpatterns = [
    path('<int:product_id>/', get_product_view, name='get_product_view'),
    path('delete/<int:product_id>/', delete_product_view, name='delete_product_view'),
    path('create/', create_product_view, name='create_product_view'),
]