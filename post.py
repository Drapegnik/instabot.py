#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/LevPasha/Instagram-API-python

import os
import random
import schedule
import time

from data import hashtags

from InstagramAPI import InstagramAPI

from src.utils import get_image, get_images, cleanup
from credentials import username, password

WAIT = True

dir = os.path.dirname(os.path.realpath(__file__))
ig = InstagramAPI(username, password)
ig.login()

def get_caption():
    return random.choice(list(hashtags.values()))

def post_image():
    image = get_image()
    ig.uploadPhoto('{}/{}'.format(dir, image), get_caption())
    cleanup([image])
    print('post image')

def post_carousel():
    photos_num = random.randint(2, 3)
    photos = get_images(photos_num)
    media = list(map(lambda file: dict({
        'type': 'photo',
        'file': '{}/{}'.format(dir, file),
    }), photos))
    ig.uploadAlbum(media, get_caption())
    cleanup(photos)
    print('post carousel with {} images'.format(photos_num))


def post():
    if random.randint(1, 10) == 7:
        post_carousel()
    else:
        post_image()


schedule.every().day.at("13:11").do(post)
schedule.every().day.at("20:35").do(post)

while WAIT:
    schedule.run_pending()
    time.sleep(1)
else:
    post()
