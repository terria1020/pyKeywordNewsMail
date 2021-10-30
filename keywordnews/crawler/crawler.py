import re
from bs4 import BeautifulSoup
import requests
import lxml.html
from lxml.html import *
from time import sleep

class CrawlerManager:
    curr_title = ""
    curr_link = ""
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
        self.url = f"https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_opt&sort=1"

    def get_contents(self) -> str:
        req = requests.get(self.url)

        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            title_search = soup.find("a", class_="news_tit")
            title = title_search['title']
            link = title_search['href']
            if self.keyword in title_search['title']:
                if CrawlerManager.curr_title != title:
                    CrawlerManager.curr_title = title
                    CrawlerManager.curr_link = link
                    contents = f"키워드 {self.keyword}에 대한 새로운 기사 글\n기사 제목: {title}\n기사 주소: {link}"
                    return contents
            else:
                return None

def main():
    pass

if __name__ == '__main__':
    cwlmgr = CrawlerManager("삼성")
    while True:
        contents = cwlmgr.get_contents()
        if contents is not None:
            print(contents)
        sleep(60)