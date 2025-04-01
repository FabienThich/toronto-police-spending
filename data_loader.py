import csv
import os

DATA_DIRECTORY = "../toronto-police-spending/data/"


def load_data(data):
    """Load data from a CSV file."""
    data_path = os.path.join(DATA_DIRECTORY, data)
    with open(data_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = [row for row in reader]
    return header, rows


BUDGET_2020 = load_data('TPS_Budget_2020.csv')
BUDGET_2021 = load_data('TPS_Budget_2021.csv')
BUDGET_2022 = load_data('TPS_Budget_2022.csv')
BUDGET_2023 = load_data('TPS_Budget_2023.csv')
BUDGET_2024 = load_data('TPS_Budget_2024.csv')
BUDGET_2025 = load_data('TPS_Budget_2025.csv')

print(BUDGET_2020)
