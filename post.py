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

ig = InstagramAPI(username, password)
ig.login()

def post():
    dir = os.path.dirname(os.path.realpath(__file__))
    caption = random.choice(list(hashtags.values()))
    photos_num = random.randint(1, 3)

    if photos_num == 1:
        print('post image')
        image = get_image()
        ig.uploadPhoto('{}/{}'.format(dir, image), caption)
        cleanup([image])
    else:
        print('post carousel')
        photos = get_images(photos_num)
        media = list(map(lambda file: dict({
            'type': 'photo',
            'file': '{}/{}'.format(dir, file),
        }), photos))
        ig.uploadAlbum(media, caption)
        cleanup(photos)

schedule.every().day.at("13:11").do(post)

while True:
    schedule.run_pending()
    time.sleep(1)
