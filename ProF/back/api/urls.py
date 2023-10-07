from django.urls import path
from . import views


urlpatterns = [
    path('category/categories', views.CategoryView.as_view(), name='category-list'),
    path('category/categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('product/<productId>', views.ProductDetailView.as_view()),
    path('product/get-products', views.ListProductsView.as_view()),
    path('product/search', views.ListSearchView.as_view()),
    path('product/related/<productId>', views.ListRelatedView.as_view()),
    path('product/by/search', views.ListBySearchView.as_view()),
    
]