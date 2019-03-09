from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from tutorial.quickstart import serializers
from tutorial.quickstart.models import DocumentRecord


class Document(GenericAPIView):
    """
    APIView to handle document files
    """
    serializer_class = serializers.DocumentSerializer

    def get(self, request):
        """
        This API is used to  get all documents
        ---
        """
        queryset = DocumentRecord.objects.filter()
        serialized_data = serializers.DocumentSerializerGET(queryset, many=True)
        return Response(data={'document_list': serialized_data.data}, status=200)

    def post(self, request):
        """
        This API is used to upload new files
        ---
        """
        serialized_data = serializers.DocumentSerializer(data=request.data, context={'request': request})
        if serialized_data.is_valid() and request.data.get('document_upload'):
            document = serialized_data.save()
            return Response(data={'id': document.id}, status=200)
        else:
            return Response(data={'error':'some error occurred'}, status=500)

    def put(self, request):
        """
        This API is used to rename files
        ---
        """
        serialized_data = serializers.DocumentSerializer(data=request.data, context={'request': request})
        if serialized_data.is_valid():
            try:
                queryset = DocumentRecord.objects.get(id=serialized_data.validated_data['id'])
            except ObjectDoesNotExist:
                return Response(data={'error': 'Id not found'}, status=500)
            document = serialized_data.update(queryset, serialized_data.validated_data)
            return Response(data={'id': document.id }, status=200)
        else:
            return Response(data={'error': 'some error occurred'}, status=500)

    def delete(self, request):
        """
        This API is used to delete files
        ---
        """
        serialized_data = serializers.DocumentSerializer(data=request.data, context={'request': request})
        if serialized_data.is_valid():
            id = serialized_data.validated_data['id']
            queryset = DocumentRecord.objects.filter(id=id).delete()
            return Response(data={'id': id }, status=200)
        else:
            return Response(data={'error': 'some error occurred'}, status=500)


