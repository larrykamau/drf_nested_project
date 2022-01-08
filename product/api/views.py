from core.api.views import CoreViewsetMixin
from rest_framework.parsers import FileUploadParser, FormParser
from core.api import NestedMultiPartParser, NestedJSONParser
from rest_framework.parsers import FormParser, FileUploadParser
from product import models
from product.api import serializers

from rest_framework import status
from rest_framework.response import Response

class ProductViewSet(CoreViewsetMixin):
    parser_classes = (NestedMultiPartParser,  NestedJSONParser, FormParser, FileUploadParser,)
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    lookup_field = "pk"
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print("=============== \n")
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
