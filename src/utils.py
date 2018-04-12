import os
from urllib import request

from PIL import Image

def get_image(i = 0):
    # get random image
    filename = 'temp{}.jpg'.format(i)
    picsum_url = 'https://picsum.photos/1000/1000/?random' # https://picsum.photos
    request.urlretrieve(picsum_url, filename)
    Image.open(filename).save(filename) # hack to get image type (eg. `jpeg`)
    return filename

def get_images(n):
    return list(map(get_image, range(n)))

def cleanup(filenames):
    for name in filenames:
        os.remove(name)
