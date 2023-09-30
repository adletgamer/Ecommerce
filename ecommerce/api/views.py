from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from ecommerceapp.models import Product


from.serializers import(
    ProductSerializer
)

class ProductView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_url_kwarg='product_id'
    serializer_class=ProductSerializer