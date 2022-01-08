
from core.api.serializers import WritableNestedModelSerializer
from product import models
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='image_gallery'
    )
    
    class Meta:
        model = models.ProductImage
        fields = '__all__'


class AssignedVariantAttributeImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='image_gallery'
    )
    class Meta:
        model = models.AssignedVariantAttributeImage
        fields = '__all__'


class AssignedVariantAttributeSerializer(WritableNestedModelSerializer):
    assigned_variant_attribute_images = AssignedVariantAttributeImageSerializer(many=True)
    
    class Meta:
        model = models.AssignedVariantAttribute
        fields = '__all__'


class AssignedVariantSerializer(WritableNestedModelSerializer):
    assigned_variant_attributes = AssignedVariantAttributeSerializer(many=True)
    
    class Meta:
        model = models.AssignedVariant
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variant
        fields = '__all__'


class ProductSerializer(WritableNestedModelSerializer):
    
    product_images = ProductImageSerializer(many=True)
    assigned_variants = AssignedVariantSerializer(many=True)
    
    class Meta:
        model = models.Product
        fields = '__all__'