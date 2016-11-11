import logging
from boto import s3
from boto.s3.key import Key

# Because of dots in bucket names: https://github.com/boto/boto/issues/421
from boto.s3.connection import ProtocolIndependentOrdinaryCallingFormat


log = logging.getLogger(__name__)

class S3ImageResizer(object):

    def __init__(self, s3_conn):
        assert s3_conn
        self.s3_conn = s3_conn
        self.image = None

    def fetch(self, url):
        """Fetch an image and keep it in memeory"""
        assert url
        raise Exception("Not implemented!")

    def resize(self, width=None, height=None):
        """Resize the in-memory image previously fetched, and
        return a clone of self holding the resized image"""
        if not width and not height:
            raise Exception("One of width or height must be specified")
        if width and height:
            raise Exception("Only one of width or height must be specified")

        raise Exception("Not implemented!")

    def store(self, to_bucket=None, key_name=None, metadata=None):
        """Store the loaded image into the given bucket with the given key name. Tag
        it with metadata if provided. Make the Image public and return its url"""

        raise Exception("Not implemented!")
