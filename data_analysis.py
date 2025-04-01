from data_loader import BUDGET_2020, BUDGET_2021, BUDGET_2022, BUDGET_2023, BUDGET_2024, BUDGET_2025
from typing import List
import doctest

class Entry:
    def __init__(self, data: str):

        """
        An entry for a row in the toronto police budget dataset.
        We are mainly interested in all the elements listed below except for _id, _organization, _command_name, _pillar_name, and _district_name

        >>> my_entry = Entry(BUDGET_2020[2])
        >>> print(my_entry)
        Entry(2, 2020, Approved Budget, 1 - Toronto Police Service, Centralized Service Charges, Centralized Service Charges, Centralized Service Charges, CCC - Central Paid Duty, Revenues, 8502, PAID DUTY- OFFICERS FEE, -24667000)
        """

        _id : int
        _year : int
        _budget_type : str
        _organization : str
        _command_name : str
        _pillar_name : str
        _district_name : str
        _unit_name : str
        _feature_category : str
        _cost_estimate : float
        _long_name : str
        _cost_actual : float

        self._id = data[0]
        self._year = data[1]
        self._budget_type = data[2]
        self._organization = data[3]
        self._command_name = data[4]
        self._pillar_name = data[5]
        self._district_name = data[6]
        self._unit_name = data[7]
        self._feature_category = data[8]
        self._cost_estimate = data[9]
        self._long_name = data[10]
        self._cost_actual = data[11]

    @property
    def year(self):
        return self._year

    @property
    def budget_type(self):
        return self._budget_type

    @property
    def unit_name(self):
        return self._unit_name

    @property
    def feature_category(self):
        return self._feature_category

    @property
    def cost_estimate(self):
        return self._cost_estimate

    @property
    def long_name(self):
        return self._long_name

    @property
    def cost_actual(self):
        return self._cost_actual

    def __str__(self):
        return f"Entry({self._id}, {self._year}, {self._budget_type}, {self._organization}, {self._command_name}, {self._pillar_name}, {self._district_name}, {self._unit_name}, {self._feature_category}, {self._cost_estimate}, {self._long_name}, {self._cost_actual})"

class Dataset:
    """
    Dataset composed of all the entries

    Columns in the dataset:
    >>> print(BUDGET_2020[0])
    ['_id', 'Fiscal_Year', 'Budget_Type', 'Organization_Entity', 'Command_Name', 'Pillar_Name', 'District_Name', 'Unit_Name', 'Feature_Category', 'Cost_Element', 'Cost_Element_Long_Name', 'Amount']

    >>> print(BUDGET_2020[1])
    ['1', '2020', 'Approved Budget', '1 - Toronto Police Service', 'Centralized Service Charges', 'Centralized Service Charges', 'Centralized Service Charges', 'CCC - Central Paid Duty', 'Revenues', '7652', 'PAID DUTY', '-1500']

    >>> my_dataset = Dataset([Entry(BUDGET_2020[1]), Entry(BUDGET_2020[2]), Entry(BUDGET_2020[3]), Entry(BUDGET_2020[4])])
    >>> print(my_dataset._data[2])
    Entry(3, 2020, Approved Budget, 1 - Toronto Police Service, Centralized Service Charges, Centralized Service Charges, Centralized Service Charges, CCC - Central Paid Duty, Revenues, 8503, PAY DUTY EQUIPMENT RENTAL, -1450000)
    """
    _data : List[Entry]

    def __init__(self, data: List[Entry]):
        self._data = data

