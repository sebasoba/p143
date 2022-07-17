import pandas as pd
import numpy as np
import csv

with open('csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
    if len(item) == 28:
        with open("final.csv", "a+") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(item)