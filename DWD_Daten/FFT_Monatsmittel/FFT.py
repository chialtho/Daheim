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
parser.add_argument('--columns', '-c', type=str, default=None,
                    help="default: all columns, else: 'B, C', 'C:E' or 'B, D:F', ...")
parser.add_argument('--skiprows', '-r', type=int, default=0,
                    help="number of lines to skip at the start of the file, default: 0")
parser.add_argument('--header', '-hr', default=None,
                    help="row to use for column labels, default: None")
parser.add_argument('--columnnames', '-n', default=None, type=str, nargs='+',
                    help="list of column names: 'name1' 'name2' ...; default: None")
parser.add_argument('--nrows', '-nr', default=None, type=int,
                    help="number of rows to parse, default: all rows")
parser.add_argument('--datanum', '-d',
                    help="number or name of data column, default: first column")

args = parser.parse_args()
filename = args.filename
sheet = args.sheet
columns = args.columns
skipr = args.skiprows
header = args.header
names = args.columnnames
rows = args.nrows



# df = pd.read_excel("Monatsmittel_T_Abweichungen.xlsx", sheet_name="TempMittel_korr",
#                    usecols="B, S", skiprows=4, header=None, names=["year", "temp"], nrows=242)

# Read data

df = pd.read_excel(filename, sheet_name=sheet, usecols=columns, skiprows=skipr, header=header, names=names, nrows=rows)

print(df)

data_temp = df[names[1]].to_numpy()

# Fast Fourier Transformation

data_temp_fft = fft(data_temp)
N = rows
rate = 1/N
data_temp_fft_freq = fftfreq(N, rate)


# print(df["year"].to_numpy()[0])
# print(data_temp)
# print(data_temp_fft)

# Plot

plt.subplot(2, 1, 1)
plt.plot(data_temp, color="#333fff")
plt.xticks(range(N), df["year"].to_numpy(), rotation="vertical")
ax = plt.gca()
temp = ax.xaxis.get_ticklabels()
temp = list(set(temp) - set(temp[::5]))
for label in temp:
    label.set_visible(False)
plt.xlabel("Years")
plt.ylabel("Temperature")
plt.title("{} to {}".format(df["year"].to_numpy()[0], df["year"].to_numpy()[0] + N - 1))

# plt.show()
plt.subplot(2, 1, 2)
plt.stem(data_temp_fft_freq, 1.0/N * np.abs(data_temp_fft[0:N]), linefmt="#333fff", markerfmt="#ff3393")
plt.ylim(0, 0.50)
plt.xlim(0, 30)
plt.xticks(np.arange(0, 30, 1.0))
plt.xlabel("Frequency (years)")
plt.ylabel("FFT power")
plt.title("Fast Fourier Transformation")
plt.grid(linestyle="--", axis='y')

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
plt.show()


# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "TempMittel_korr" -c "B,Q" -r 4 -n "year" "temp" -nr 242

# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "SummSonne" -c "A,N" -r 14 -n "year" "temp" -nr 76

# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "T_Anom_total" -c "A,AB" -r 4 -n "year" "temp" -nr 242

# python3 .\FFT.py -f "Monatsmittel_T_Abweichungen.xlsx" -s "SummRR" -c "A,N" -r 4 -n "year" "temp" -nr 144
