from storage_connector import StorageConnector

class AzureConnector(StorageConnector):

    def __init__(self):
        super().__init__()
        print('using azure connector')
        self.aws_access_key = None
        self.aws_secret_key = None
        self.bucket_name = None
        self.s3_url_prefix = None

    def set_credentials(self):
        self.aws_access_key = 'asdasd'
        # self.aws_secret_key = settings.AWS_SECRET_ACCESS_KEY
        # self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        # self.s3_url_prefix = settings.AWS_URL

    def upload_to_object_store(self, destination_path, file_object, file_type=None, key_required=True):
        pass

    def download_from_object_store(self):
        pass


    def rename_obect(self, document_id, new_name):
        pass
