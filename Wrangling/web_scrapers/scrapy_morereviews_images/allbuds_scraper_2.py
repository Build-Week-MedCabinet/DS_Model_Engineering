import scrapy
import csv
import re


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
    if raw_string == None:
        return

    clean_string = raw_string.strip('\n')
    clean_string = ' '.join(clean_string.split())
    return clean_string


def clean_strain_name(raw_name):
    """
    Post process strain names
    """
    strain_name = clean_string(raw_name)
    strain_name = strain_name.split(' Strain')[0]
    return strain_name


def get_strain_type_percentage(raw, strain_type):
    try:
        processed_strain_info = raw.split('/')
    except:
        if raw:
            return ('100%' + ' ' + raw).strip()
        return None

    for info in processed_strain_info:
        if strain_type in info.lower():
            if len(info.split(' ')) > 1:
                return info.strip()


def summarize_thc_data(thc_data):
    try:
        thc_values = re.findall(r'\d+', thc_data)
    except:
        return None

    if len(thc_values) > 1:
        thc_values = [int(value) for value in thc_values]
        return sum(thc_values)/len(thc_values)

    elif len(thc_values) == 1:
        return thc_values[0]

    return None


# def parse_cbd_cbn(em_fields):
#     data_out = []
#     for item in em_fields:
#         data_out.append(clean_string(item))
#     return ' '.join(data_out)


class AllbudSpider2(scrapy.Spider):
    name = 'allbud_spider'
    start_urls = get_allbud_urls('allbuds_1.csv', 'desc_url')

    def parse(self, response):
        # # From view-source in Mozilla.  These parameters were manually discovered
        DESC_TEXT_SELECTOR = '.strain-description-mobile::text'
        STRAIN_NAME_SELECTOR = 'h1::text'
        STRAIN_TYPE_SELECTOR = '.description h4::text'
        STRAIN_TYPE_PERCENTAGE = '.strain-percentages::text'
        EFFECT_SELECTOR = '#positive-effects .tags-list a::text'
        FLAVOR_SELECTOR = '#flavors .tags-list a::text'
        AROMA_SELECTOR = '#aromas .tags-list a::text'
        COMPONENT_SELECTOR_THC = '.percentage::text'
        # COMPONENT_SELECTOR_CBD_CBN = '.percentage em::text' # Not currently implemented.  Problems with data validation.

        # # Build output object
        strain_desc = clean_string(response.css(DESC_TEXT_SELECTOR).extract_first())
        strain_name = clean_strain_name(response.css(STRAIN_NAME_SELECTOR).get())
        strain_effects = ' '.join(response.css(EFFECT_SELECTOR).getall())
        strain_flavors = ' '.join(
            set(response.css(FLAVOR_SELECTOR).getall() + response.css(AROMA_SELECTOR).getall())
            )
        strain_thc = summarize_thc_data(clean_string(response.css(COMPONENT_SELECTOR_THC).get()))
        # strain_cbd = response.css(COMPONENT_SELECTOR_CBD_CBN).getall() # Still Under Development
        strain_percent_indica = get_strain_type_percentage(response.css(STRAIN_TYPE_PERCENTAGE).get(),'indica')
        strain_percent_sativa = get_strain_type_percentage(response.css(STRAIN_TYPE_PERCENTAGE).get(),'sativa')
        strain_type = clean_string(response.css(STRAIN_TYPE_SELECTOR).extract_first())


        # Write to file
        filename = "allbuds_strain_data.csv"

        with open(filename, 'a+', newline='') as csvfile:
            spider_writer = csv.writer(csvfile, delimiter=',')
            spider_writer.writerow([
                strain_name,
                strain_desc,
                strain_type,
                strain_percent_indica,
                strain_percent_sativa,
                strain_thc,
                # strain_cbd, # Not currently implemented. Problems with data validation
                strain_flavors,
                strain_effects
                ])

        # yield {
        #     'strain_desc': strain_desc,
        #     'strain_name': strain_name,
        # }


