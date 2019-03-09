from rest_framework import serializers
from tutorial.quickstart import models
from django.conf import settings
from tutorial.quickstart.file_storage import Storage


class DocumentSerializer(serializers.ModelSerializer):
    """
    Document
    """
    document_upload = serializers.FileField()
    name = serializers.CharField()
    new_name = serializers.CharField()
    id = serializers.IntegerField()

    class Meta:
        model = models.DocumentRecord
        fields = ('id', 'name', 'document_upload', 'new_name')


    def create(self, validated_data):
        file_object = validated_data['document_upload']
        name = validated_data['name']
        storage_obj = Storage(filename=name, file_object=file_object)
        return storage_obj.save_file()


    def update(self, instance, validated_data):
        instance.name = validated_data.get('new_name', instance.name)
        instance.save()
        return instance


    def get_fields(self, *args, **kwargs):
        fields = super(DocumentSerializer, self).get_fields(*args, **kwargs)
        if self.context.get('request').method == 'POST':
            fields.pop('id')
            fields.pop('new_name')
        elif self.context.get('request').method == 'PUT':
            fields.pop('name')
            fields.pop('document_upload')
            for field in fields.values():
                field.required = True
        elif self.context.get('request').method == 'DELETE':
            fields.pop('name')
            fields.pop('document_upload')
            fields.pop('new_name')
            for field in fields.values():
                field.required = True
        return fields


class DocumentSerializerGET(serializers.ModelSerializer):

    class Meta:
        model = models.DocumentRecord
        fields = ('name', 'id', 'document_url', 'modified_at', 'created_at')



