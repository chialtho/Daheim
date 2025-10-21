#! /usr/bin/env python3
import argparse as ap

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq

# Parser

parser = ap.ArgumentParser()

parser.add_argument('--filename', '-f', type=str, required=True, help="path to xlsx file")
parser.add_argument('--sheet', '-s', type=str, required=True, help="name of the excel sheet")
parser.add_argument('--column', '-c', type=str, default="A",
                    help="default: A, else: 'B', 'C', ...")
parser.add_argument('--skiprows', '-r', type=int, default=0,
                    help="number of lines to skip at the start of the file, default: 0")
parser.add_argument('--header', '-hr', default=None,
                    help="row to use for column labels, default: None")
parser.add_argument('--nrows', '-nr', default=None, type=int,
                    help="number of rows to parse, default: all rows")


args = parser.parse_args()
filename = args.filename
sheet = args.sheet
column = args.column
skipr = args.skiprows
header = args.header
rows = args.nrows


# Read data

df = pd.read_excel(filename, sheet_name=sheet, usecols=column, skiprows=skipr, header=header,names=["data"], nrows=rows)

print(df)

data_temp = df["data"].to_numpy()

# Fast Fourier Transformation

data_temp_fft = fft(data_temp)
N = rows
rate = 1/N
data_temp_fft_freq = fftfreq(N, rate)

# Plot

plt.stem(data_temp_fft_freq, 1.0/N * np.abs(data_temp_fft[0:N]), linefmt="#333fff", markerfmt="#ff3393")
plt.ylim(0, 0.50)
plt.xlim(0, 30)
plt.xticks(np.arange(0, 30, 1.0))
plt.xlabel("Frequency (years)")
plt.ylabel("FFT power")
plt.title("Fast Fourier Transformation")
plt.grid(linestyle="--", axis='y')

plt.show()


# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "TempMittel_korr" -c "Q" -r 4 -nr 242

# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "SummSonne" -c "N" -r 14 -nr 76

# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "T_Anom_total" -c "AB" -r 4 -nr 242

# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "SummRR" -c "N" -r 4 -nr 144
