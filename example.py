import os
import sys
import logging
from boto import s3
from s3imageresizer import S3ImageResizer

# Logging setup
log = logging.getLogger(__name__)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)
# EOF logging setup. Pfew.


conn = s3.connect_to_region(
    'eu-west-1',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)

i = S3ImageResizer(conn)

i.fetch('http://www.gokqsw.com/images/picture/picture-4.jpg')


