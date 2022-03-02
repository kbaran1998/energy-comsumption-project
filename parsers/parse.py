"""Extractor for PowerLog3 CSV files."""
import os
import csv
from page_list import pages
import pandas as pd

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


def calculate_mean_and_std_for_frameworks():
    """Method that calculates mean and std for each framework"""
    data={"framework":[],  "Processor Power_0(Watt) (mean)":[]}
    for framework in pages:
        data["framework"].append(framework)
        out_path = os.path.dirname(os.path.realpath(__file__))
        out_path = os.path.dirname(out_path)
        out_path = os.path.join(out_path, "out")
        out_path_files = [os.path.join(out_path, f) for f in os.listdir(out_path)
                      if os.path.isfile(os.path.join(out_path, f)) and framework in f]
        framework_pds = [pd.read_csv(item) for item in out_path_files]
        result = pd.concat(framework_pds)
        mean = result['Processor Power_0(Watt)'].mean()
        std = result['Processor Power_0(Watt)'].std()
        data[ "Processor Power_0(Watt) (mean)"].append(mean)
    df = pd.DataFrame(data=data)
    print(df.to_markdown())

def calculate_mean_and_std_for_websites():
    """Method that calculates mean and std for each framework"""
    data={"website":[], "link":[], "framework":[], "Processor Power_0(Watt) (mean)":[], "Processor Power_0(Watt) (std)":[]}
    for framework in pages:
        for website in pages[framework]:
            data["website"].append(website[0])
            data["link"].append(website[1])
            data["framework"].append(framework)
            out_path = os.path.dirname(os.path.realpath(__file__))
            out_path = os.path.dirname(out_path)
            out_path = os.path.join(out_path, "out")
            out_path_files = [os.path.join(out_path, f) for f in os.listdir(out_path)
                          if os.path.isfile(os.path.join(out_path, f)) and website[0] in f]
            framework_pds = [pd.read_csv(item) for item in out_path_files]
            result = pd.concat(framework_pds)
            mean = result['Processor Power_0(Watt)'].mean()
            std = result['Processor Power_0(Watt)'].std()
            data["Processor Power_0(Watt) (mean)"].append(mean)
            data["Processor Power_0(Watt) (std)"].append(std)
    df = pd.DataFrame(data=data)
    print(df.to_markdown())

parse_all_output_files()
print("Frameworks")
calculate_mean_and_std_for_frameworks()
print("Websites")
calculate_mean_and_std_for_websites()
