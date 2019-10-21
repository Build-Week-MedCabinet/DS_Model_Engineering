import scrapy
import csv


def get_allbud_urls(filename, columns):
    """
    Reads as file and fetches one of the columns, returning a list of datapoints in that column.

    Parameters
    ----------
    params: tuple-like object
        (path, column)
        path: string or path instance to .csv or .txt file containing urls
        column: column name

    Returns
    -------
    list
        Returns list of URL's in that column
    """
    import pandas as pd
    import os
    path = os.path.join(os.getcwd(), filename)


    data = pd.read_csv(path)

    return data[columns].tolist()


def clean_string(raw_string):
    """
    Remove return lines and whitespace from string of text

    Parameters
    ----------
    raw_string: str

    Returns
    -------
    str
        string stripped of \n and trailing, leading, whitespace

    """
    clean_string = raw_string.strip('\n')
    clean_string = ' '.join(clean_string.split())
    return clean_string

class AllbudSpider2(scrapy.Spider):
    name = 'allbud_spider'
    start_urls = get_allbud_urls('allbuds_1.csv', 'desc_url')

    def parse(self, response):
        # # From view-source in Mozilla.  These parameters were manually discovered
        DESC_TEXT_SELECTOR = '.strain-description-mobile::text'
        STRAIN_NAME_SELECTOR = 'h1::text'

        # # Build output object
        strain_desc = clean_string(response.css(DESC_TEXT_SELECTOR).extract_first())
        strain_name = clean_string(response.css(STRAIN_NAME_SELECTOR).get())
        strain_effects = None # Implement
        strain_flavors = None # ' '.join(set(Flavors + Aromas)))
        strain_thc = None
        strain_cbd = None
        strain_type = None


        # Write to file
        filename = "allbuds_2.csv"

        with open(filename, 'a+', newline='') as csvfile:
            spider_writer = csv.writer(csvfile, delimiter=',')
            spider_writer.writerow([strain_name, strain_desc])

        # yield {
        #     'strain_desc': strain_desc,
        #     'strain_name': strain_name,
        # }


