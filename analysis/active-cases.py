# Computes active cases from daily case totals

import csv
from argparse import ArgumentParser
from rich.console import Console
from rich.table import Table


def read_csv(filename):
    with open(filename, "rt", newline="") as infile:
        reader = csv.reader(infile)
        return list(reader)[1:]


def compute_active_cases(data):
    output = []
    for i in range(10, len(data)+1):
        window = data[i-10:i]
        staff = sum(int(rec[1]) for rec in window)
        students = sum(int(rec[2]) for rec in window)
        other = sum(int(rec[3]) for rec in window)
        total = sum(int(rec[4]) for rec in window)
        output.append((window[-1][0], staff, students, other, total))
    return output


def display_active_cases(data):
    console = Console()
    table = Table(title="Active Coronavirus Cases, University of Leeds")
    table.add_column("Period End")
    table.add_column("Staff", justify="right")
    table.add_column("Students", justify="right")
    table.add_column("Other", justify="right")
    table.add_column("Total", justify="right")
    for row in data:
        table.add_row(row[0], str(row[1]), str(row[2]), str(row[3]), str(row[4]))
    with console.pager():
        console.print(table)


def write_csv(data, filename):
    with open(filename, "wt", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(("Period End", "Staff", "Students", "Other", "Total"))
        writer.writerows(data)


def parse_command_line():
    parser = ArgumentParser(
        description="Computes active cases by day from daily case totals.",
        epilog="Active cases are tabulated on screen if no output file is specified."
    )
    parser.add_argument(
        "-o", metavar="FILENAME", dest="outfile",
        help="name for output file"
    )
    parser.add_argument(
        "infile", metavar="FILENAME",
        help="name of daily cases CSV file"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line()
    daily_cases = read_csv(args.infile)
    active_cases = compute_active_cases(daily_cases)
    if args.outfile:
        write_csv(active_cases, args.outfile)
    else:
        display_active_cases(active_cases)
