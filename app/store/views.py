from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.store.models import Products
from app.store.serializers import ProductSerializer


class ListProducts(APIView):
    allowed_methods = ['GET', 'POST']

    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
