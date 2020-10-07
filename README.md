# uol-covid

This repository contains a CSV file of aggregated coronavirus case
data scraped from the University of Leeds website, along with Python
code for the scraper.

## Scraper Usage Examples

To scrape case data and write to a new file:

    python uol-covid.py cases.csv

To scrape case data and append to an existing file:

    python uol-covid.py -a cases.csv

## Scraper Dependencies

* Requests
* BeautifulSoup 4
