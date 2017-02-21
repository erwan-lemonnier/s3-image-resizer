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
logging.getLogger('boto').setLevel(logging.INFO)
# EOF logging setup. Pfew.


conn = s3.connect_to_region(
    S3_REGION,
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)

i = S3ImageResizer(conn)

i.fetch('http://s3-eu-west-1.amazonaws.com/pnt-item-pictures-incoming/item_58412fc768022a5112b0b110_000002/0.jpg')

url = i.store(
    in_bucket=BUCKET_NAME,
    key_name='raw.jpg'
)
log.info("Got url %s" % url)

# Should be 'https://pnt-tests.s3-eu-west-1.amazonaws.com/raw.jpg'
want = 'https://%s.s3-%s.amazonaws.com:443/%s' % (BUCKET_NAME, S3_REGION, 'raw.jpg')
assert url == want, '%s == %s' % (url, want)

# apply exif orientation, if any
i.orientate()

# resize to width 200
ii = i.resize(width=200)
url_w200 = ii.store(
    in_bucket=BUCKET_NAME,
    key_name='raw_w200.jpg'
)
log.info("Got url %s" % url_w200)

# Should get 'https://pnt-tests.s3-eu-west-1.amazonaws.com/raw_w200.jpg'
want = 'https://%s.s3-%s.amazonaws.com:443/%s' % (BUCKET_NAME, S3_REGION, 'raw_w200.jpg')
assert url_w200 == want, '%s == %s' % (url_w200, want)

# resize to height 200
ii = i.resize(height=200)
url_h200 = ii.store(
    in_bucket=BUCKET_NAME,
    key_name='raw_h200.jpg'
)
log.info("Got url %s" % url_h200)

# resize to a 100 square
ii = i.resize(width=100, height=100)
url_w100_h100 = ii.store(
    in_bucket=BUCKET_NAME,
    key_name='raw_w100_h100.jpg'
)
log.info("Got url %s" % url_w100_h100)
