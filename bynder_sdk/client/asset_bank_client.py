from .upload_client import UploadClient


class AssetBankClient:
    """ Client used for all the operations that can be done to the
    Bynder Asset Bank.
    """
    def __init__(self, bynder_request_handler):
        self.bynder_request_handler = bynder_request_handler
        self.upload_client = UploadClient(bynder_request_handler)

    def brands(self):
        """ Gets list of the brands.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/v4/brands/'
        )

    def tags(self, query: dict = None):
        """ Gets list of the tags.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/v4/tags/',
            params=query or {}
        )

    def meta_properties(self, query: dict = None):
        """ Gets list of the meta properties.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/v4/metaproperties/',
            params=query or {}
        )

    def media_list(self, query: dict = None):
        """ Gets a list of media assets filtered by parameters.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/v4/media/',
            params=query or {}
        )

    def media_info(self, media_id, versions: dict = None):
        """ Gets all the media information for a specific media id.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/v4/media/{0}/'.format(media_id),
            params=versions or {}
        )

    def media_download_url(self, media_id, query: dict = None):
        """ Gets the download file URL for a specific media id.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/v4/media/{0}/download/'.format(media_id),
            params=query or {}
        )

    def set_media_properties(self, media_id, query: dict = None):
        """ Updates the media properties (metadata) for a specific media id.
        """
        return self.bynder_request_handler.post(
            endpoint='/api/v4/media/{0}/'.format(media_id),
            payload=query or {}
        )

    def delete_media(self, media_id):
        """ Deletes a media asset.
        """
        return self.bynder_request_handler.delete(
            endpoint='/api/v4/media/{0}/'.format(media_id)
        )

    def create_usage(self, integration_id, asset_id, query: dict = None):
        """ Creates a usage record for a media asset.
        """
        if query is None:
            query = {}
        query['integration_id'] = integration_id
        query['asset_id'] = asset_id
        return self.bynder_request_handler.post(
            endpoint='/api/media/usage/',
            payload=query
        )

    def usage(self, query: dict = None):
        """ Gets all the media assets usage records.
        """
        return self.bynder_request_handler.get(
            endpoint='/api/media/usage/',
            params=query or {}
        )

    def delete_usage(self, integration_id, asset_id, query: dict = None):
        """ Deletes a usage record of a media asset.
        """
        if query is None:
            query = {}
        query['integration_id'] = integration_id
        query['asset_id'] = asset_id
        return self.bynder_request_handler.delete(
            endpoint='/api/media/usage/',
            params=query
        )

    def upload_file(self, file_path, brand_id, media_id: str = '', query: dict = None):
        """ Upload file.
        """
        if query is None:
            query = {}
        query['brandId'] = brand_id
        self.upload_client.upload(
            file_path=file_path,
            media_id=media_id,
            upload_data=query
        )
