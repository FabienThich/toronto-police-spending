import csv
import os

DATA_DIRECTORY = "../toronto-police-spending/data/"


def load_data(data):
    """Load data from a CSV file."""
    data_path = os.path.join(DATA_DIRECTORY, data)
    dataset = []

    with open(data_path, newline= '') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            dataset.append(row)

    return dataset


BUDGET_2020 = load_data('TPS_Budget_2020.csv')
BUDGET_2021 = load_data('TPS_Budget_2021.csv')
BUDGET_2022 = load_data('TPS_Budget_2022.csv')
BUDGET_2023 = load_data('TPS_Budget_2023.csv')
BUDGET_2024 = load_data('TPS_Budget_2024.csv')
BUDGET_2025 = load_data('TPS_Budget_2025.csv')

# 'Feature category' and 'Cost Element' values are swapped for the 2023 dataset.
for row in BUDGET_2023:
    row[8],row[9] = row[9],row[8]

# Slice index by one because those are headers
BUDGET_ALL_YEARS = BUDGET_2020 + BUDGET_2021[1:] + BUDGET_2022[1:] + BUDGET_2023[1:] + BUDGET_2024[1:] + BUDGET_2025[1:]

# print(type(BUDGET_ALL_YEARS))
# print(BUDGET_2020[0])
# print(BUDGET_2020[4])