
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from django.forms.models import model_to_dict
from rest_framework.parsers import (
    MultiPartParser, FormParser, JSONParser, FileUploadParser,
)

class CoreViewsetMixin(ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    # parser_classes = (NestedMultiPartParser,  NestedJSONParser, FormParser, FileUploadParser,)

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = super().get_queryset().filter(is_deleted=False)
        ids = self.request.query_params.get('ids', None)
        if ids:
            ids_list = ids.split(',')
            queryset = queryset.filter(id__in=ids_list)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

        # return Response(status=status.HTTP_204_NO_CONTENT)

    # def perform_destroy(self, instance):
    #     instance.is_deleted = True
    #     instance.save(update_fields=['is_deleted'])

    @action(methods=['delete'], detail=False )
    def bulk_delete(self, request, *args, **kwargs):

        ids = self.request.query_params.get('ids', None)
        print(ids)
        data = []
        if ids:
            ids_list = ids.split(',')
            for i in ids_list:
                item = get_object_or_404(self.serializer_class.Meta.model, pk=int(i))
                data.append(model_to_dict(item))
                item.delete()
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'message': "'ids' param not defined"}
            )

        return Response(status=status.HTTP_204_NO_CONTENT, data=data)



