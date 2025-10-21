#!/usr/bin/env python


import csv
import matplotlib.pyplot as plt


if __name__=="__main__":
    data_size = 0

    with open("data/iris/iris.data", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            pass
        # print(reader.line_num)
        data_size = reader.line_num



    dimensions = [1, 2, 3, 4]
    density = []

    for dim in dimensions:
        dens = data_size / (10 ** dim)
        density.append(dens)

    print(density)


    plt.plot([1, 2, 3, 4], density)
    plt.xlabel("Dimension")
    plt.ylabel("Density")
    plt.title("Density of iris data set")
    plt.grid(True)
    plt.show()

