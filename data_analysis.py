from data_loader import BUDGET_2020, BUDGET_2021, BUDGET_2022, BUDGET_2023, BUDGET_2024, BUDGET_2025

class Entry:
    def __init__(self, id, year, budget_type, organization, command_name, pillar_name, district_name, unit_name, feature_category, cost_estimate, long_name, cost_actual):

        """
        An entry for a row in the toronto police budget dataset.
        We are mainly interested in all the elements listed below except for _id, _organization, _command_name, _pillar_name, and _district_name
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

        self._id = id
        self._year = year
        self._budget_type = budget_type
        self._organization = organization
        self._command_name = command_name
        self._pillar_name = pillar_name
        self._district_name = district_name
        self._unit_name = unit_name
        self._feature_category = feature_category
        self._cost_estimate = cost_estimate
        self._long_name = long_name
        self._cost_actual = cost_actual

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

