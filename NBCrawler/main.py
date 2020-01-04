#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : main.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 04.01.2020
# Last Modified Date: 04.01.2020
# Last Modified By  : JCHRYS <jchrys@me.com>
import settings
import platform
import time
import json
import os
from NBCrawler.core import utils
from NBCrawler.core.requester import Request

from pprint import pprint

## os_valdation ##
if (platform.system() != 'Darwin'):
    print('your OS is not supported')
    exit()
##TODO header, params, url 
print("=======give me your keyword")
request = Request(settings.default_headers, settings.default_params, settings.default_url)
keyword = input()
res = request.search(keyword).json()
detail_ids = ['authorIntroContent', 'bookIntroContent', 'tableOfContentsContent']
items = res['items']
print(len(items))

for item in items:
    detail_dict = utils.get_html_content_by_id(item['link'], detail_ids)
    item.update(detail_dict)
    for key in item.keys():
        item[key] = utils.drop_html_tag_all(item[key])
    

with open(os.path.join(settings.path_to_output, 'filename.json'), 'w', encoding='utf8') as file:
    json.dump(items, file, ensure_ascii=False, indent=4)
