import sys
import re
from icrawler.builtin import GoogleImageCrawler


# Get URL of the image
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

    google_crawler = GoogleImageCrawler(storage={'root_dir': 'web_scraper/crawled'})
    google_crawler.downloader.logger.addFilter(checkCrawlURL)

    # Searches for malignant spots (TOTAL: 78 IMGS):
        # skin cancer spots
        # early stage skin cancer
        # malignant skin spots
        # skin cancer images
        # câncer de pele imagens
        # basal cell carcinoma
        # squamous cell carcinoma
        # merkel cell cancer
        # melanoma

    # Searches for benign spots (TOTAL: 64 IMGS):
        # harmless dark spots on skin
        # normal dark spots on skin
        # common dark spots on skin
        # freckles
        # melasma
        # lentigines
        # seborrheic keratosis
        # healthy dark spots
        # pintas saudaveis na pele
        # pintas benignas na pele
        # sinais cutâneos saudáveis
        # pintas inofensivas na pele
        # manchas cutâneas inofensivas
        # healthy melanocytic spots

    google_crawler.crawl(keyword='healthy melanocytic spots', max_num=1000)

    # Save the urls in a .txt
    with open('web_scraper/links.txt', 'w') as f:
        for i in all_urls:
            f.write(i+"\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
