# Scrapes UoL coronavirus stats page and outputs data to a CSV file

import csv
import sys
import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://coronavirus.leeds.ac.uk/statistics-and-support-available/"


def extract_table():
    request = requests.get(URL, headers={
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"
    })

    doc = BeautifulSoup(request.text, "html.parser")
    table = doc.find("table")

    # Sanity check that this is the table we want
    # (should be preceded by "confirmed coronavirus cases")

    prev_tag = table.find_previous_sibling()
    assert prev_tag.name == "p"
    text = str(prev_tag.string).lower()
    assert text.startswith("confirmed coronavirus cases")

    return table


def extract_data(table):
    rows = table.find_all("tr")
    assert len(rows) == 4

    dates = rows[0].find_all("td")
    staff_counts = rows[1].find_all("td")
    student_counts = rows[2].find_all("td")
    totals = rows[3].find_all("td")
    assert len(dates) == len(staff_counts)
    assert len(staff_counts) == len(student_counts)
    assert len(student_counts) == len(totals)

    data = [("Date", "Staff", "Students", "Total")]

    for i in range(1, len(dates)):
        dt = datetime.strptime(dates[i].string, "%d %B %Y")
        data.append((dt.date().isoformat(), staff_counts[i].string,
            student_counts[i].string, totals[i].string))

    return data


def write_csv(data, filename):
    with open(filename, "wt") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


if __name__ == "__main__":
    if not sys.argv[1:]:
        sys.exit("Usage: python uol-covid.py <csv-filename>")

    table = extract_table()
    data = extract_data(table)
    write_csv(data, sys.argv[1])
