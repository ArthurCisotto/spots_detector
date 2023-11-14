import sys
import re

from icrawler.builtin import GoogleImageCrawler

all_urls = []

def checkCrawlURL(log_input):
    # re-print captured log message
    print("INFO - downloader -", log_input.getMessage())
    # extract url
    res = re.search(r"image #\d+\t(.*)", log_input.getMessage())
    if res:
       # add extracted url to list
       all_urls.append(res.group(1))




def main():


    google_crawler = GoogleImageCrawler(storage={'root_dir': 'crawled'})
    google_crawler.downloader.logger.addFilter(checkCrawlURL)

    google_crawler.crawl(keyword='pig', max_num=20)

    with open('links.txt', 'w') as f:
        for i in all_urls:
            f.write(i+"\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())
