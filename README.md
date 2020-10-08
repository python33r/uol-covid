# uol-covid

This repository contains a CSV file of aggregated coronavirus case data
scraped [from the University of Leeds website][uol], along with Python code
for the scraper.

## Scraper Usage Examples

To scrape case data and write to a new file:

    python uol-covid.py cases.csv

To scrape case data and append to an existing file:

    python uol-covid.py -a cases.csv

## Scraper Dependencies

* [Requests][req]
* [BeautifulSoup 4][bs]

To install, create and activate a Python 3 virtual environment, then do

    pip install -r requirements.txt

[uol]: https://coronavirus.leeds.ac.uk/statistics-and-support-available/
[req]: https://requests.readthedocs.io/en/master/
[bs]: https://www.crummy.com/software/BeautifulSoup/
