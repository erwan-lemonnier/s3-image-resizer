import os
import sys
import logging
from boto import s3
from s3imageresizer import S3ImageResizer

# Demonstrate module usage and asserts its behavior (I know, this is not a
# proper test suite...)
#
# Requirements:
# 1. Set the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
# 2. Set S3_REGION and BUCKET_NAME to whatever fits you
#
# Run:
# python example.py

S3_REGION = 'eu-west-1'
BUCKET_NAME = 'pnt-tests'

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
    S3_REGION,
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)

i = S3ImageResizer(conn)

i.fetch('http://www.gokqsw.com/images/picture/picture-4.jpg')

url = i.store(
    in_bucket=BUCKET_NAME,
    key_name='raw.jpg'
)
log.info("Got url %s" % url)
# Should be 'https://pnt-tests.s3-eu-west-1.amazonaws.com/raw.jpg'
want = 'https://%s.s3-%s.amazonaws.com/%s' % (BUCKET_NAME, S3_REGION, 'raw.jpg')
assert url == want, '%s == %s' % (url, want)
