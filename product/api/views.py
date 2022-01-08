import random
import string
from core.api.views import CoreViewsetMixin

from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.parsers import FileUploadParser, FormParser


from core.api import NestedMultiPartParser, NestedJSONParser

from rest_framework.parsers import (
    FormParser, JSONParser, FileUploadParser,
)
from product import models
from product.api import serializers


class ProductViewSet(CoreViewsetMixin):
    parser_classes = (NestedMultiPartParser,  NestedJSONParser, FormParser, FileUploadParser,)
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    lookup_field = "pk"
