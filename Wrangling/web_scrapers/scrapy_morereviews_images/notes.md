# Notes for scrapy web scraper

Implementation of scrapy library to get various labelled datasets from website repositories where API not available.

## Main Sites Requiring Scraping

* PotGuides
* allbud.com
* Leafly
* Wikileaf

### AllBuds Notes

Site cookies confuse getting the images out.  It looks like you can grab the image directly from /strain-name.jpg without using the token hash.

https://media.allbud.com/resized/350x242/media/feature/strain/bruce-banner.jpg?t=95852100dfa792c31faf804bbb710dd35c42dbdbbbde94bdbf076a284ace4d39

> Most Recent Scrapes

> (2019-10-21 20:30MT) allbuds_strain_data.csv

**Build Notes** 1

Building series of scrapers, saves, transforms, that have to be executed manually in sequence.  Follow websiteName_1 ,.._2, etc.

**Running Scrapy Spiders**

From Command Line:

> scrapy runspdier <filename.py>