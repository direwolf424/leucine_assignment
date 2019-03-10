from storage_connector import StorageConnector

class S3Connector(StorageConnector):

    def __init__(self):
        super().__init__()
        print('using s3 connector')
        pass

    def set_credentials(self):
        self.aws_access_key = 'asdasd'
        # self.aws_secret_key = settings.AWS_SECRET_ACCESS_KEY
        # self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        # self.s3_url_prefix = settings.AWS_URL

    def save_to_object_store(self, destination_path, file_object, file_type=None, key_required=True):
        pass

    def get_from_object_store(self):
        pass


    def rename_obect(self, document_id, new_name):
        pass


x = S3Connector()