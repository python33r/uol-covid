# uol-covid

This repository contains

* A CSV file of aggregated coronavirus case data scraped [from the University of Leeds website][uol]
* Python code for the scraper
* Python code to process and analyze the data

## Scraper Usage Examples

To scrape case data and write to a new file:

    python daily-cases.py cases.csv

To scrape case data and update an existing CSV file:

    python daily-cases.py --update cases.csv

Note: if the newly-scraped data contains records whose dates match existing
records, those existing records will be replaced by the new data.

## Analysis Examples

To derive day-by-day active cases from a CSV file of daily case reports:

    python active-cases.py cases.csv

This will display the active cases on screen as a table.  To output the
active cases to a file, do

    python active-cases.py -o active.csv cases.csv

## Dependencies

* [Requests][req]
* [BeautifulSoup 4][bs]
* [Rich][rich] 9.0.0 or newer (not required for scraper)

To use the scripts, create and activate a Python 3 virtual environment,
then do

    pip install -r requirements.txt

[uol]: https://coronavirus.leeds.ac.uk/statistics-and-support-available/
[req]: https://requests.readthedocs.io/en/master/
[bs]: https://www.crummy.com/software/BeautifulSoup/
[rich]: https://rich.readthedocs.io/en/latest/introduction.html
