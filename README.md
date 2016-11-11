# s3pictresizer

A python module to import and resize pictures into amazon S3 storage.

## Warning

This module is a MVP. It works fine on its golden path, which is importing
jpegs from well-behaved CDNs, resizing them in memory and storing the results
in S3.

## Synopsis

Typical usecase:

```
# Initialize an S3ImageResizer:
# s3_conn = s3.connect_to_region(...)
i = S3ImageResizer(s3_conn)

# Fetch an image into memory
i.fetch('http://www.gokqsw.com/images/picture/picture-4.jpg')

# Resize the image and store it to S3
i.resize(
    width=200
).store(
    to_bucket='my-images',
    key_name='image-w200-jpg'
)

# And once more, with a different size
i.resize(
    height=200
).store(
    to_bucket='my-images',
    key_name='image-h200-jpg'
)
```

## Installation

s3pictresizer requires Pillow, which in turn needs external libraries.
On ubuntu, you would for example need:

```
sudo apt-get install libjpeg8 libjpeg8-dev libopenjpeg-dev
```

Then

```
pip install s3pictresizer
```