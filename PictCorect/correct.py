# -*- coding: utf-8 -*-

import get_image

classgetimage = get_image.getImage()
extensions = ".jpg", ".jpeg", ".png"
url = ''
f = open('source.txt', 'rt')
texts = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()

for text in texts:
	# クロール開始
    url = text.replace('\n', '')
    url = url.replace('\r','')
    print(url)
    classgetimage.crawring(url, extensions)
