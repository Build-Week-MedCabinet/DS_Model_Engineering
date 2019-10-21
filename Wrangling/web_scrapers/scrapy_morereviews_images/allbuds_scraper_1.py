import scrapy
import re
import csv


class AllbudSpider(scrapy.Spider):
    name = 'allbud_spider'
    start_urls = ['https://www.allbud.com/marijuana-strains/search?results=8000']

    def parse(self, response):
        SET_SELECTOR = ".feature"
        for feature_header in response.css(SET_SELECTOR):
            # From view-source in Mozilla.  These parameters were manually discovered
            IMAGE_URL_SELECTOR = 'a img::attr(data-src)'
            FEATURE_URL_SELECTOR = 'a ::attr(href)'
            BASE_URL = 'https://www.allbud.com'

            # Build output object
            img_url = get_image_url(feature_header.css(IMAGE_URL_SELECTOR).extract_first())
            feature_url = BASE_URL + feature_header.css(FEATURE_URL_SELECTOR).extract_first()

            # Write to file
            filename = "allbuds_1.csv"

            with open(filename, 'a', newline='') as csvfile:
                spider_writer = csv.writer(csvfile, delimiter=',')
                spider_writer.writerow([img_url, feature_url])

            # yield {
            #     # 'img_name': get_strain_name()
            #     'img_url': img_url,
            #     'feature_url': feature_url,
            # }


def get_image_url(input_sequence):
    """
    Parameters
    ----------
    raw_output: string
        Output from Scrapy .css selector.

    Returns
    -------
    list
        URLs matching htt* pattern
    """
    # pull url from input sequence
    url = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', input_sequence)[0]

    # strip end of url
    url = url.split('?')[0]

    return url
