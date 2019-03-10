from s3_connector import S3Connector
from local_storage_connector import LocalStorageConnector
from azure_connector import AzureConnector


class ObjectStoreConnectorFactory():

    @staticmethod
    def get_connector(cloud_name):
        if cloud_name == "aws":
            s3_connector = S3Connector()
            s3_connector.set_credentials()
            return s3_connector
        elif cloud_name == "local":
            local_connector = LocalStorageConnector()
            local_connector.set_credentials()
            return local_connector
        elif cloud_name == "azure":
            azure_connector = AzureConnector()
            azure_connector.set_credentials()
            return azure_connector