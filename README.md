# uol-covid

This repository contains a CSV file of aggregated coronavirus case data
scraped [from the University of Leeds website][uol], along with Python code
for the scraper.

## Scraper Usage Examples

To scrape case data and write to a new file:

    python uol-covid.py cases.csv

To scrape case data and update an existing CSV file:

    python uol-covid.py --update cases.csv

Note: if the newly-scraped data contains records whose dates match existing
records, those existing records will be replaced by the new data.

## Scraper Dependencies

* [Requests][req]
* [BeautifulSoup 4][bs]

To install, create and activate a Python 3 virtual environment, then do

    pip install -r requirements.txt

[uol]: https://coronavirus.leeds.ac.uk/statistics-and-support-available/
[req]: https://requests.readthedocs.io/en/master/
[bs]: https://www.crummy.com/software/BeautifulSoup/
