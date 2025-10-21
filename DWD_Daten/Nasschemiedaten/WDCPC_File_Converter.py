#! /usr/bin/env python3

import argparse as ap

# import numpy as np
import pandas as pd
# import csv

# Parser

parser = ap.ArgumentParser()


parser.add_argument('--start', '-s', type=int, required=True,
                    help="First year")
parser.add_argument('--end', '-e', type=int, required=True,
                    help="Last year")


args = parser.parse_args()
start = args.start
end = args.end

file_header = f"WDCPC-DB-r{start}.xlsm"
df = pd.read_excel(file_header, sheet_name="DB", usecols="A:BX", skiprows=52, header=None, nrows=4)
df.to_csv(f"WDCPC_{start}_{end}.csv", mode='w', sep=";", header=False, index=False)

for i in range(end-start+1):
    filename = f"WDCPC-DB-r{start+i}.xlsm" 
    rows = 365
    print(i)
    if (start + i) % 4 == 0:
        rows = 366
    df = pd.read_excel(filename, sheet_name="DB", usecols="A:BX", skiprows=56, header=None, nrows=rows)
    # print(df.iloc[:, 10:20])
    df.to_csv(f"WDCPC_{start}_{end}.csv", mode='a', sep=";", header=False, index=False)
   
