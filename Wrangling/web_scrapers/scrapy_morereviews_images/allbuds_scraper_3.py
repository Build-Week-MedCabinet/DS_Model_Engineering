"""
    Image Downloader
"""
import urllib3

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

def parse_name_from_url(url):
    section = url.split('strain/')[-1]
    filename = section.split('/')[0]
    return section, filename

http = urllib3.PoolManager()


url_list = get_allbud_urls('allbuds_1.csv', 'image_url')

for i in range(100):
    print(parse_name_from_url(url_list[i]))