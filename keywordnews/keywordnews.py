
from .mailhandler.textbuilder import set_text
from .mailhandler.sender import sender
from .crawler.crawler import *

class pyKeyNewsSVC:
    def __init__(self, keyword, _to) -> None:
        self.keyword = keyword
        self._to = _to
        self.cwlmgr = CrawlerManager(keyword)

    def start(self):
        while True:
            contents = self.cwlmgr.get_contents()
            if contents is not None:
                message = set_text(self._to, contents, self.keyword)
                sender.send(message, self._to)
            sleep(5)