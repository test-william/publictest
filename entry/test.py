#encoding:utf8

from keywords import sendurl
import re

html = sendurl.get("http://www.taobao.com/")
print(html)
link = re.findall('href=.+?[ |>]', html)
print(link)
for l in link:
    print(l)