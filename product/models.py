import os

from django.db import models

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnDiscPlaceholderImage

class Product(models.Model):
    name = models.CharField(max_length=100)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE, blank=True, null=True)
    image = VersatileImageField(
        # 'Optional Image',
        # upload_to='image_gallery/',
        # blank=True,
        # placeholder_image=OnDiscPlaceholderImage(
        #     path=os.path.join(
        #         os.path.dirname(os.path.abspath(__file__)),
        #         'placeholder.gif'
        #     )
        # )
        
        'Image',
        upload_to='image_gallery/',
        width_field='width',
        height_field='height'
        # =========
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True,
        default=400
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True,
        default=400
    )


class Variant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


class Attribute(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    variant = models.ForeignKey(Variant, related_name="attributes", blank=True, null=True, on_delete=models.CASCADE)
    # name = models.ManyToManyField(Site)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # access_key = models.ForeignKey(AccessKey, null=True, on_delete=models.CASCADE)
    
    
class AssignedVariant(models.Model):
    product = models.ForeignKey(Product, related_name='assigned_variants', on_delete=models.CASCADE, blank=True, null=True)
    variant = models.ForeignKey(Variant, related_name='assigned_product_variants', on_delete=models.CASCADE, blank=True, null=True)
    

class AssignedVariantAttribute(models.Model):
    sku = models.CharField(max_length=100, blank=True, null=True)
    assigned_variant = models.ForeignKey(AssignedVariant, related_name='assigned_variant_attributes', on_delete=models.CASCADE, blank=True, null=True)


class AssignedVariantAttributeImage(models.Model):
    assigned_variant_attribute = models.ForeignKey(AssignedVariantAttribute, related_name='assigned_variant_attribute_images', on_delete=models.CASCADE, blank=True, null=True)
    image = VersatileImageField(
        'Image',
        upload_to='image_gallery/',
        width_field='width',
        height_field='height'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True,
        default=400
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True,
        default=400
    )