from data_loader import BUDGET_2020, BUDGET_2021, BUDGET_2022, BUDGET_2023, BUDGET_2024, BUDGET_2025, BUDGET_ALL_YEARS
from typing import List, Optional, Dict
import doctest

class Entry:
    def __init__(self, data: str):

        """
        An entry for a row in the toronto police budget dataset.
        We are mainly interested in all the elements listed below except for _id, _organization, _command_name, _pillar_name, and _district_name, _cost_element

        >>> my_entry = Entry(BUDGET_2020[2])
        >>> print(my_entry)
        Entry(2, 2020, Approved Budget, 1 - Toronto Police Service, Centralized Service Charges, Centralized Service Charges, Centralized Service Charges, CCC - Central Paid Duty, Revenues, 8502, PAID DUTY- OFFICERS FEE, -24667000.0)
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
        _cost_element : str
        _long_name : str
        _cost_estimate : float

        self._id = int(data[0])
        self._year = int(data[1])
        self._budget_type = str(data[2])
        self._organization = str(data[3])
        self._command_name = str(data[4])
        self._pillar_name = str(data[5])
        self._district_name = str(data[6])
        self._unit_name = str(data[7])
        self._feature_category = str(data[8])
        self._cost_element = str(data[9])
        self._long_name = str(data[10])
        self._cost_estimate = float(str(data[11].replace(',','')))

    @property
    def id(self):
        return self._id

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

    def __str__(self):
        return f"Entry({self._id}, {self._year}, {self._budget_type}, {self._organization}, {self._command_name}, {self._pillar_name}, {self._district_name}, {self._unit_name}, {self._feature_category}, {self._cost_element}, {self._long_name}, {self._cost_estimate})"

class Dataset:
    """
    Dataset composed of all the entries

    Columns in the dataset:
    >>> print(BUDGET_ALL_YEARS[0])
    ['_id', 'Fiscal_Year', 'Budget_Type', 'Organization_Entity', 'Command_Name', 'Pillar_Name', 'District_Name', 'Unit_Name', 'Feature_Category', 'Cost_Element', 'Cost_Element_Long_Name', 'Amount']

    >>> print(Entry(BUDGET_2020[1]))
    Entry(1, 2020, Approved Budget, 1 - Toronto Police Service, Centralized Service Charges, Centralized Service Charges, Centralized Service Charges, CCC - Central Paid Duty, Revenues, 7652, PAID DUTY, -1500.0)

    >>> my_dataset = Dataset([Entry(BUDGET_2020[1]), Entry(BUDGET_2020[2]), Entry(BUDGET_2020[3]), Entry(BUDGET_2020[4])])
    >>> print(my_dataset._data[2])
    Entry(3, 2020, Approved Budget, 1 - Toronto Police Service, Centralized Service Charges, Centralized Service Charges, Centralized Service Charges, CCC - Central Paid Duty, Revenues, 8503, PAY DUTY EQUIPMENT RENTAL, -1450000.0)
    """
    _data : List[Entry]

    def __init__(self, data: List[Entry]):
        self._data = data

    @property
    def data(self):
        return self._data

    def division_filter(self, division_number: Optional[int] = None) -> List[Entry]:
        """
        Filters the dataset to only contain entries with the specified division.
        If no police division is provided, return all the entries with a division value in the unit_name attribute.

        >>> data = Dataset([Entry(row) for row in BUDGET_2020[455:460]])
        >>> print([x.unit_name for x in data.division_filter()])
        ['Division 12', 'Division 12', 'Division 12', 'Division 12', 'Division 12']
        >>> data = Dataset([Entry(row) for row in BUDGET_2020[802:805]])
        >>> print([x.id for x in data.division_filter(51)])
        [803, 804]
        """
        result = []

        if division_number is None:
            result = [row for row in self.data if 'division' in row.unit_name.lower()]
           
        else:
            result = [row for row in self.data if f'division {division_number}' in row.unit_name.lower()]

        return result

    def division_summary(self) -> Dict[str, float]:
        """
        returns a summary of all the individual police divisions. They are sorted from divisions with the greatest to least accumulated budget
        :return:
        >>> data = Dataset([Entry(row) for row in BUDGET_2020[1:]])
        >>> result_data = data.division_summary()
        >>> print(result_data)
        {'division 55': 86667845.56, 'division 41': 67248663.45, 'division 51': 66399777.29, 'division 14': 65282817.65, 'division 52': 61139801.5, 'division 43': 60995862.34, 'division 31': 55822911.8, 'division 23': 55371084.11, 'division 32': 52578103.09, 'division 42': 51723490.07, 'division 22': 49815000.06, 'division 11': 49190022.35, 'division 12': 48791360.88, 'division 53': 39459667.76, 'division 13': 39251704.59, 'division 33': 37575703.9}
        >>> print(result_data.keys())
        dict_keys(['division 55', 'division 41', 'division 51', 'division 14', 'division 52', 'division 43', 'division 31', 'division 23', 'division 32', 'division 42', 'division 22', 'division 11', 'division 12', 'division 53', 'division 13', 'division 33'])
        >>> print(list(result_data.items())[:3])
        [('division 55', 86667845.56), ('division 41', 67248663.45), ('division 51', 66399777.29)]
        >>> print(list(result_data.items())[-3:])
        [('division 53', 39459667.76), ('division 13', 39251704.59), ('division 33', 37575703.9)]
        """
        grouped_data = {}

        for row in self.division_filter():
            division_name = row.unit_name.lower()

            if division_name not in grouped_data:
                grouped_data[division_name] = 0

            grouped_data[division_name] += abs(row.cost_estimate)

        grouped_data = {division: round(estimate, 2) for division, estimate in grouped_data.items()}

        result_data = dict(sorted(grouped_data.items(), key=lambda x: x[1], reverse=True))
        # print(result_data)

        return result_data


    def when_year(self, year: int) -> List[Entry]:
        """
        Returns a dataset of the year specified

        :param year:
        :return: List[Entry]

        >>> data = Dataset([Entry(BUDGET_2020[1]), Entry(BUDGET_2022[1])])
        >>> print(data.when_year(2020)[0])
        Entry(1, 2020, Approved Budget, 1 - Toronto Police Service, Centralized Service Charges, Centralized Service Charges, Centralized Service Charges, CCC - Central Paid Duty, Revenues, 7652, PAID DUTY, -1500.0)
        """

        filtered_dataset = []

        for entry in self._data:
            if int(entry.year) == year:
                filtered_dataset.append(entry)

        return filtered_dataset


    def calculate_cost_estimate(self, absolute: int = 0) -> float:
        """
        Returns the sum costs of a dataset. The absolute paramter is used for calculating the cost estimate with its absolute values.
        0 means to calculate without taking the absolute value of the cost_estiate, 1 means to calculate with the absolute value.
        :return: float

        >>> data = Dataset([Entry(row) for row in BUDGET_2020[1:5]])
        >>> print([x.cost_estimate for x in data._data])
        [-1500.0, -24667000.0, -1450000.0, -3700000.0]
        >>> print(data.calculate_cost_estimate())
        -29818500.0
        >>> data = Dataset([Entry(row) for row in BUDGET_2020[1:]])
        >>> print(data.calculate_cost_estimate())
        2249095580.08
        >>> print(data.calculate_cost_estimate(1))
        2849263017.86
        """
        result = 0
        for row in self._data:
            if absolute == 1:
                try:
                    result += abs(float(str(row.cost_estimate).replace(',', '')))
                except ValueError:
                    pass
                    # print(f"Skipping invalid cost_estimate value: {row.cost_estimate}")

            else:
                try:
                    result += float(str(row.cost_estimate).replace(',',''))
                except ValueError:
                    pass
                    # print(f"Skipping invalid cost_estimate value: {row.cost_estimate}")

        return round(result, 2)

    def no_cost_estimate(self):
        """
        returns the number of 0 entries for cost_estimate
        >>> data_2020 = Dataset([Entry(row) for row in BUDGET_2020[1:]])
        >>> print(data_2020.no_cost_estimate())
        1544
        >>> data_2021 = Dataset([Entry(row) for row in BUDGET_2021[1:]])
        >>> print(data_2021.no_cost_estimate())
        0
        >>> data_2022 = Dataset([Entry(row) for row in BUDGET_2022[1:]])
        >>> print(data_2022.no_cost_estimate())
        3475
        >>> data_2023 = Dataset([Entry(row) for row in BUDGET_2023[1:]])
        >>> print(data_2023.no_cost_estimate())
        9191
        >>> data_2024 = Dataset([Entry(row) for row in BUDGET_2024[1:]])
        >>> print(data_2024.no_cost_estimate())
        5129
        >>> data_2025 = Dataset([Entry(row) for row in BUDGET_2025[1:]])
        >>> print(data_2025.no_cost_estimate())
        5120
        """
        count = 0

        for row in self.data:
            if row.cost_estimate == 0:
                count += 1

        return count

    def category(self, category: str = None) -> float:
        """
        Returns the cost estimate for a specific feature category. Users who do not pass
        a parameter to get will get the sum of cost estimate for 'Not_Used'

        Not_Used
        Salaries
        Premium Pay
        Benefits
        Materials & Supplies
        Equipment
        Services
        Revenues

        :param category:
        :return: List[Entry]
        >>> data = Dataset([Entry(row) for row in BUDGET_2020[1:]])
        >>> print(data.category('Salaries'))
        1682088970.66
        >>> print(data.category('Premium Pay'))
        108388261.93
        >>> data = Dataset([Entry(row) for row in BUDGET_2021[1:]])
        >>> print(data.category('Salaries'))
        1700132754.43
        >>> data = Dataset([Entry(row) for row in BUDGET_2022[1:]])
        >>> print(data.category('Salaries'))
        1734134200.0
        >>> data = Dataset([Entry(row) for row in BUDGET_2023[1:]])
        >>> print(data.category('Salaries'))
        1817939697.73
        >>> print(data.category('Premium Pay'))
        152513405.47
        """
        sum = 0

        if category is None:
            for row in self.data:
                if row.feature_category == 'Not_Used':
                    sum += row.cost_estimate

        else:
            for row in self.data:
                if category in row.feature_category:
                    sum += row.cost_estimate

        return round(sum, 2)

    def category_summary(self) -> Dict[str, float]:
        """
        Returns a summary of all the feature categories with their total cost estimates, sorted from the greatest to least accumulated budget.

        >>> data = Dataset([Entry(row) for row in BUDGET_2020[1:]])
        >>> result = data.category_summary()
        >>> print(result)
        {'Salaries': 1697999070.22, 'Benefits': 450207787.95, 'Revenues': 285502876.04, 'Services': 229693764.44, 'Premium Pay': 121991811.75, 'Materials & Supplies': 45030286.94, 'Equipment': 18837420.52}
        >>> print(Dataset([Entry(row) for row in BUDGET_2021[1:]]).category_summary())
        {'Salaries': 1723847396.57, 'Benefits': 482721110.33, 'Revenues': 300853483.03, 'Services': 201122840.73, 'Premium Pay': 121373249.58, 'Materials & Supplies': 45681993.79, 'Equipment': 19081443.96}
        >>> print(Dataset([Entry(row) for row in BUDGET_2022[1:]]).category_summary())
        {'Salaries': 1750624702.0, 'Benefits': 507433586.0, 'Revenues': 313390335.0, 'Services': 208761051.0, 'Premium Pay': 142050712.0, 'Materials & Supplies': 50192731.0, 'Equipment': 17432490.0}
        >>> print(Dataset([Entry(row) for row in BUDGET_2023[1:]]).category_summary())
        {'Salaries': 1843629238.35, 'Benefits': 538193251.28, 'Revenues': 370540168.9, 'Services': 221043789.02, 'Premium Pay': 153737005.47, 'Materials & Supplies': 53463877.8, 'Equipment': 26648572.44, 'Not_Used': 0.0}
        >>> print(Dataset([Entry(row) for row in BUDGET_2024[1:]]).category_summary())
        {'Salaries': 992908800.0, 'Benefits': 289209400.0, 'Revenues': 190149400.0, 'Services': 97587200.0, 'Premium Pay': 62212000.0, 'Materials & Supplies': 29959000.0, 'Equipment': 7777700.0, 'Not_Used': 0.0}
        >>> print(Dataset([Entry(row) for row in BUDGET_2025[1:]]).category_summary())
        {'Salaries': 993505100.0, 'Benefits': 307027600.0, 'Revenues': 201254100.0, 'Services': 103312400.0, 'Premium Pay': 64412000.0, 'Materials & Supplies': 29698000.0, 'Equipment': 9495900.0, 'Not_Used': 0.0}

        """
        grouped_data = {}

        for row in self.data:
            category_name = row.feature_category
            if '-' in category_name and category_name[0].isdigit():

                # Some entries were entered with a prefix: '1-Salaries' and 'Salaries' were used interchangeably
                category_name = category_name.split('-')[1].strip()

            if category_name not in grouped_data:
                grouped_data[category_name] = 0

            grouped_data[category_name] += abs(row.cost_estimate)

        grouped_data = {category: round(estimate,2) for category, estimate in grouped_data.items()}

        result_data = dict(sorted(grouped_data.items(), key=lambda x: x[1], reverse=True))

        return result_data

# print([x.cost_actual for x in data_2023._data[1:10]])
