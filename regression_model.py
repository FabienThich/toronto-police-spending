import math

from PIL.ImageOps import scale
from matplotlib import pyplot as plt
from typing import List

from data import *
from data_analysis import *


class LinearRegression:
    """A linear regression model to predict the cost estimate if you give it a category
    """

    def __init__(self) -> None:
        """Return a LinearRegression abstraction."""
        self.type = ''
        self.a = 0  # intercept of regression line
        self.b = 0  # slope of regression line
        self.xs = []  # x values used to train model
        self.ys = []  # y values used to train model
        self.r_squared = 0  # r-squared value of model (how well it fits the training data)

    def train(self, entries: List[Entry]) -> None:
        """
        Train the regression model using a list of police budget entries.
        Assumes each Entry object has a 'cost_estimate', by performing least-squares linear regression.
        Save the R^2 value and the parameters of this model as attributes of `self`.


        >>> load_data = BUDGET_2020 + BUDGET_2021[1:] + BUDGET_2022[1:] + BUDGET_2023[1:] + BUDGET_2024[1:]
        >>> filter_data = [row for row in load_data[1:] if row[-1] != 0]
        >>> data = Dataset([Entry(row) for row in filter_data])
        >>> model = LinearRegression()
        >>> model.train(data.data)
        >>> round(model.a,2)
        119957491.61
        >>> round(model.b,2)
        -59175.1
        >>> model.r_squared
        0.0012822746619163491
        """

        self.xs = [entry.year for entry in entries]
        self.ys = [abs(entry.cost_estimate) for entry in entries]

        mean_x = sum(self.xs) / len(self.xs)
        mean_y = sum(abs(x) for x in self.ys) / len(self.ys)

        sxx = sum((x - mean_x) ** 2 for x in self.xs)
        syy = sum((y - mean_y) ** 2 for y in self.ys)

        sxy = 0

        for i in range(len(self.xs)):
            sxy += (self.xs[i] - mean_x) * (self.ys[i] - mean_y)

        self.b = sxy / sxx
        self.a = mean_y - self.b * mean_x
        self.r_squared = (sxy ** 2) / (sxx * syy)


    def predict(self, year: int) -> float:
        """Use the parameters of the regression model to predict an overall rating for 2026.

        >>> model = LinearRegression()
        >>> model.a = 119957491.61
        >>> model.b = -59175.1
        >>> round(model.predict(2025),2)
        127914.11
        >>> round(model.predict(2026),2)
        68739.01
        """

        return self.b * year + self.a

    
    def make_predictions(self, entries: List[Entry]) ->  Dict[Entry, float]:
        """
        returns the predicted budget for each entry
        >>> data_all = BUDGET_2020[1:] + BUDGET_2021[1:] + BUDGET_2022[1:] + BUDGET_2023[1:] + BUDGET_2024[1:]
        >>> new_data_all = Dataset([Entry(row) for row in data_all[1:]])
        >>> model = LinearRegression()
        >>> model.a = 119957491.61
        >>> model.b = -59175.1
        >>> predictions = model.make_predictions(new_data_all.data)
        >>> predictions[new_data_all.data[0]]
        423789.6099999994
        >>> predictions[new_data_all.data[-1]]
        187089.21000000834
        """

        result = {}

        for entry in entries:
            # print(entry, entry.year)
            result[entry] = self.predict(entry.year)

        return result


def calculate_mse(predictions: dict[Entry, float]) -> float:
    """
    Calculate the mean squared error between predicted ratings and actual ratings
    >>> data_all = BUDGET_2020[1:] + BUDGET_2021[1:] + BUDGET_2022[1:] + BUDGET_2023[1:] + BUDGET_2024[1:]
    >>> new_data_all = Dataset([Entry(row) for row in data_all[1:]])
    >>> model = LinearRegression()
    >>> model.a = 119957491.61
    >>> model.b = -59175.1
    >>> predictions = model.make_predictions(new_data_all.data)
    >>> calculate_mse(predictions)
    4805479727053.9
    """

    sse = 0
    n = len(predictions)

    for entry, predicted in predictions.items():
        actual = entry.cost_estimate
        sse += (predicted - actual) ** 2

    return sse / n


