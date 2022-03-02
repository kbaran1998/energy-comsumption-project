"""Extractor for PowerLog3 CSV files."""
import os
import csv

def extract_and_save_csv(original_file, file_to_save_to):
    """Gets the wanted columns from the CSV file which in this case are:
    - System Time,Elapsed Time (sec),
    - Processor Power_0(Watt),
    - Cumulative Processor Energy_0(Joules),
    - Cumulative Processor Energy_0(mWh)

    Usage:
    extract_and_save_csv('Vue_9gag_1.csv', 'Vue_9gag_1.csv')
    """
    with open(original_file, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows_csv = []
        for row in reader:
            rows_csv.append(row)
        timed_data = rows_csv[:-19]

    with open(file_to_save_to, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in timed_data:
            new_row = []
            new_row.append(row[0])
            new_row.append(row[2])
            new_row.append(row[5])
            new_row.append(row[6])
            new_row.append(row[7])
            writer.writerow(new_row)

def parse_all_output_files():
    """Parser for all output files in 'out' folder."""
    out_path = os.path.dirname(os.path.realpath(__file__))
    out_path = os.path.dirname(out_path)
    out_path = os.path.join(out_path, "out")
    out_path_files = [os.path.join(out_path, f) for f in os.listdir(out_path)
                      if os.path.isfile(os.path.join(out_path, f))]
    for file in out_path_files:
        extract_and_save_csv(file, file)

parse_all_output_files()
