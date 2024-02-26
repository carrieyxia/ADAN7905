# 1. Install and Setup Visual Studio CodeLinks to an external site. by following the instructions in the link
# 2. Write a python program that prints “Hello World”

import sys
import pandas as pd
import numpy as np
import random
print("Hello World")

# 3. Write Python program exploring key packages and modules


def randNum_lst(x):
    """This function returns a list of x number of random integer from 1 to 10."""
    numbers = []
    i = 0
    while i < x:
        numbers.append(random.randint(1, 10))
        i += 1
    return numbers


print(randNum_lst(3))

# 4. From SKLearn or best practices of Python Programming  links - write code using Numpy and Pandas


# Generate a NumPy array using randNum_lst function
numpy_array = np.array([randNum_lst(3), randNum_lst(3)])
# print(numpy_array)

# Create a Pandas DataFrame from the NumPy array
df = pd.DataFrame(numpy_array, columns=['A', 'B', 'C'])

# Print the DataFrame
print("Pandas DataFrame:")
print(df)

# Perform operations with NumPy
mean_value = np.mean(df)
sum_values = np.sum(df)

# Print the results
print("\nNumPy Operations:")
print(f"Mean of column: {mean_value}")
print(f"Sum of columns: {sum_values}")


# 5. Copy an example from SKLearn from previous week’s exercise and execute in debug mode for every line
# Inspect variable defined in the code by printing to Debug console
# Modify and test code in Debug consoles.


symbol_dict = {
    "TOT": "Total",
    "XOM": "Exxon",
    "CVX": "Chevron",
    "COP": "ConocoPhillips",
    "VLO": "Valero Energy",
    "MSFT": "Microsoft",
    "IBM": "IBM",
    "TWX": "Time Warner",
    "CMCSA": "Comcast",
    "CVC": "Cablevision",
    "YHOO": "Yahoo",
    "DELL": "Dell",
    "HPQ": "HP",
    "AMZN": "Amazon",
    "TM": "Toyota",
    "CAJ": "Canon",
    "SNE": "Sony",
    "F": "Ford",
    "HMC": "Honda",
    "NAV": "Navistar",
    "NOC": "Northrop Grumman",
    "BA": "Boeing",
    "KO": "Coca Cola",
    "MMM": "3M",
    "MCD": "McDonald's",
    "PEP": "Pepsi",
    "K": "Kellogg",
    "UN": "Unilever",
    "MAR": "Marriott",
    "PG": "Procter Gamble",
    "CL": "Colgate-Palmolive",
    "GE": "General Electrics",
    "WFC": "Wells Fargo",
    "JPM": "JPMorgan Chase",
    "AIG": "AIG",
    "AXP": "American express",
    "BAC": "Bank of America",
    "GS": "Goldman Sachs",
    "AAPL": "Apple",
    "SAP": "SAP",
    "CSCO": "Cisco",
    "TXN": "Texas Instruments",
    "XRX": "Xerox",
    "WMT": "Wal-Mart",
    "HD": "Home Depot",
    "GSK": "GlaxoSmithKline",
    "PFE": "Pfizer",
    "SNY": "Sanofi-Aventis",
    "NVS": "Novartis",
    "KMB": "Kimberly-Clark",
    "R": "Ryder",
    "GD": "General Dynamics",
    "RTN": "Raytheon",
    "CVS": "CVS",
    "CAT": "Caterpillar",
    "DD": "DuPont de Nemours",
}

symbols, names = np.array(sorted(symbol_dict.items())).T

quotes = []

for symbol in symbols:
    print("Fetching quote history for %r" % symbol, file=sys.stderr)
    url = (
        "https://raw.githubusercontent.com/scikit-learn/examples-data/"
        "master/financial-data/{}.csv"
    )
    quotes.append(pd.read_csv(url.format(symbol)))

close_prices = np.vstack([q["close"] for q in quotes])
open_prices = np.vstack([q["open"] for q in quotes])
