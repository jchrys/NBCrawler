import re
import requests
from bs4 import BeautifulSoup


re_all = re.compile('<[^>]*>')
def drop_html_tag_all(html):
    return re.sub(re_all, '', html)

def get_drop_html_tag_but(tag):
    regex = '(?!</?' + tag + '>)<.*?>'
    #print(regex)
    _re = re.compile(regex)
    def drop_html_tag(html):
        return re.sub(_re, '', html)
    return drop_html_tag 



def get_detail(item: dict, url, keys_to_update) -> None:
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup

if __name__ == '__main__':
    print(drop_html_tag_all("<strong> Hello World!</strong>"))
    br_cleaner = get_drop_html_tag_but('all')
    print(br_cleaner("<br>GOOODDADSAD<br>>"))
    get_detail_test_url = 'http://book.naver.com/bookdb/book_detail.php?bid=15433261'
    print(get_detail(1, get_detail_test_url, 1))
     
