# to run from root dir: `python software/read_html_file.py`
# source: https://wiki.python.org/moin/MiniDom

import code # to debug: `code.interact(local=locals())`
import os
from bs4 import BeautifulSoup

#
# READ HTML FILE
#

menu_dot_html = os.path.abspath(__file__).replace(os.path.relpath(__file__), "menu-items/index.html")

print "READING HTML FILE -- %(file_name)s" % {"file_name": menu_dot_html}

soup = BeautifulSoup(open(menu_dot_html),"lxml")

#
# SEARCH FILE CONTENTS
#

menu_item_list = soup.find(id="menu-item-list")

print menu_item_list

#
# MANIPULATE FILE CONTENTS
#

for i in [1,2,3,4,5]:
    list_item = soup.new_tag('li')
    list_item.string = str(i)
    menu_item_list.append(list_item)

print menu_item_list

print soup
