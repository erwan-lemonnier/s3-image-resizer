import logging
import requests
from PIL import Image
from StringIO import StringIO
from boto import s3
from boto.s3.key import Key


log = logging.getLogger(__name__)


class S3ImageResizerException(Exception):
    pass

class InvalidParameterException(S3ImageResizerException):
    pass

class CantFetchImageException(S3ImageResizerException):
    pass

class RTFMException(S3ImageResizerException):
    pass


class S3ImageResizer(object):

    def __init__(self, s3_conn):
        if not s3_conn or 'S3Connection' not in str(type(s3_conn)):
            raise InvalidParameterException("Expecting an instance of boto s3 connection")
        self.s3_conn = s3_conn
        self.image = None

    def fetch(self, url):
        """Fetch an image and keep it in memory"""
        assert url
        log.debug("Fetching image at url %s" % url)
        res = requests.get(url)
        if res.status_code != 200:
            raise CantFetchImageException("Failed to load image at url %s" % url)
        self.image = Image.open(StringIO(res.content))

    def resize(self, width=None, height=None):
        """Resize the in-memory image previously fetched, and
        return a clone of self holding the resized image"""
        if not width and not height:
            raise InvalidParameterException("One of width or height must be specified")
        if width and height:
            raise InvalidParameterException("Only one of width or height must be specified")
        if not self.image:
            raise RTFMException("No image loaded! You must call fetch() before resize()")

        raise Exception("Not implemented!")

    def store(self, to_bucket=None, key_name=None, metadata=None):
        """Store the loaded image into the given bucket with the given key name. Tag
        it with metadata if provided. Make the Image public and return its url"""

        raise Exception("Not implemented!")
