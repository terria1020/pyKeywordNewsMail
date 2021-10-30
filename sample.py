
from keywordnews.keywordnews import pyKeyNewsSVC

def main():
    service = pyKeyNewsSVC("삼성", "jaehan1346@gmail.com")
    service.start()

if __name__ == '__main__':
    main()