from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import argparse

class TitleCrawler:
    """Accepts a base url to crawl from"""
    def __init__(self, start_url):
        self.urls_to_visit = []
        self.urls_to_visit.append(start_url)
        self.visited = []
        self.domain = 'https://' + urlparse(start_url).netloc

    def start(self):
        for url in self.urls_to_visit:
            self.crawl(url)

    def crawl(self, link):
        page_content = requests.get(link).text
        soup = BeautifulSoup(page_content, "html.parser")
        title = soup.find('title')
        print('Page being crawled: ', title.text, link)
        self.visited.append(link)
        urls = soup.find_all('a')

        for url in urls:
            url = url.get('href')

            if url is not None and url.startswith(self.domain) and url not in self.visited:
                self.urls_to_visit.append(url)
                print('Crawled this many pages so far: ', len(self.visited))
                print('There are still ', len(self.urls_to_visit), ' left to crawl')


def main():
    # todo: take urls from command line args. add db. tests
    # parser = argparse.ArgumentParser(description=)
    # site = 
    crawler = TitleCrawler('http://wikipedia.com')
    crawler.start()

if __name__ == '__main__':
    main()
