#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/LevPasha/Instagram-API-python

import os
import random
from urllib import request
from PIL import Image

from InstagramAPI import InstagramAPI

from credentials import username, password
from data import hashtags

# get random image
dir = os.path.dirname(os.path.realpath(__file__))
filename = 'temp.jpg'
picsum_url = 'https://picsum.photos/1000/1000/?random' # https://picsum.photos
request.urlretrieve(picsum_url, filename)
Image.open(filename).save(filename) # hack to get image type (eg. `jpeg`)

# set some hashtags
caption = random.choice(list(hashtags.values()))

# post it!
InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()
InstagramAPI.uploadPhoto('{}/{}'.format(dir, filename), caption)

# cleanup
os.remove(filename)
