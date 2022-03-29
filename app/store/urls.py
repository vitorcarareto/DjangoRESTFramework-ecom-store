from django.urls import path
from .views import ListProducts

app_name = 'store'

urlpatterns = [
    path('products/', ListProducts.as_view(), name='products'),
    path('products/<int:pk>/', ListProducts.as_view()),
]
