from django.conf import settings
from tutorial.quickstart.models import DocumentRecord
import uuid

class Storage:

    def __init__(self, filename, file_object):
        self.filename = filename
        self.file_object = file_object
        self.storage = settings.FILE_STORAGE

    def save_in_s3(self):
        data = {}
        data['storage'] = settings.FILE_STORAGE
        # here we need to use boto3 to actually upload to s3
        data['document_url'] = 'https://cdn-images-1.medium.com/max/1600/1*Q6O661l2bPf6piXpVH6-ag.png'
        data['name'] = self.filename
        return DocumentRecord.objects.create(**data)


    def save_in_local(self):
        uuid_code = str(uuid.uuid4())
        file_path = settings.MEDIA_ROOT + uuid_code
        with open(file_path, 'wb+') as destination:
            for chunk in self.file_object.chunks():
                destination.write(chunk)
            url = settings.MEDIA_URL + uuid_code
            return self.save_to_db(document_url=url, document_location=destination.name)

    def save_file(self):
        if settings.FILE_STORAGE == settings.S3_STORAGE:
            return self.save_in_s3()
        elif settings.FILE_STORAGE == settings.LOCAL_STORAGE:
            return self.save_in_local()

    def save_to_db(self, document_url=None, document_location=None):
        data = {}
        data['storage'] = self.storage
        # here we need to use boto3 to actually upload to s3
        if document_url:
            data['document_url'] = document_url
        if document_location:
            data['document_location'] = document_location
        data['name'] = self.filename
        return DocumentRecord.objects.create(**data)
