from django.urls import path
from . import views
from .views import ListProductsView

urlpatterns = [
    path('categories', views.CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('product/<productId>', views.ProductDetailView.as_view()),
    path('get-products', ListProductsView.as_view(), name='list-products'),
    path('search', views.ListSearchView.as_view()),
    path('related/<productId>', views.ListRelatedView.as_view()),
    path('by/search', views.ListBySearchView.as_view()),
]