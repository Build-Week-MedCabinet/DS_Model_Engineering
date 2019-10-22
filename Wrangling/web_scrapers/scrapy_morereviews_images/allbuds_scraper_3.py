"""
    Image Downloader
"""
import wget
import os
import numpy as np
from time import time, sleep
from multiprocessing import Process


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

def parse_filename_from_url(url):
    # Get the strain section from the image URL
    section = url.split('strain/')[-1]
    # Take name from section information
    return url.split('/')[-1]


# Get updated list of urls and features (for image paths, names)
img_url_list = get_allbud_urls('allbuds_1.csv', 'image_url')
desc_url_list = get_allbud_urls('allbuds_1.csv', 'desc_url')

# Set Fetch params
batch_size = 10
save_path = os.path.join(os.getcwd(), 'images')


class Downloader():
    def __init__(self, batch_size=10, num_threads=6, delay=0.1):
        self.file_names = [parse_filename_from_url(desc_url) + '.jpg' for desc_url in desc_url_list]
        self.img_urls = img_url_list
        self.num_threads = num_threads
        self.delay = delay

    def download_file(self, url, filepath):
        """
        Download file at url to specified filepath

        Parameters
        ----------
        url: str
            url pointing to file

        filepath: str or path object
            absolute path string or file path of save location
        """
        try:
            wget.download(url, filepath)
        except:
            return False

    def create_jobs(self):
        """
        Create batches of jobs (list of lists) to map download handler onto
        """
        assert len(self.file_names) == len(self.img_urls)
        self.master_list = np.array(list(zip(self.file_names, self.img_urls)))

        self.jobs = np.array_split(self.master_list, self.num_threads)

    def download_batch(self, batch):
        for file_params in batch:
            self.download_file(file_params[1], file_params[0])
            sleep(self.delay)

    def execute(self):
        start = time()
        procs = []
        for batch in self.jobs:
            # Create process and store reference
            proc = Process(target=self.download_batch, args=(batch,))
            procs.append(proc)
            # Start process
            proc.start()
        # Wait for processes to finish and close
        for proc in procs:
            proc.join()
        stop = time()

        print('{} Jobs completed in {}'.format(len(procs), stop-start))


if __name__ == "__main__":
    downloader = Downloader()
    downloader.create_jobs()
    downloader.execute()
    # print(downloader.jobs)