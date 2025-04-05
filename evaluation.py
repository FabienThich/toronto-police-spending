from data_analysis import *

print('Year   |    Cost Estimate\n')
data_2020 = Dataset([Entry(row) for row in BUDGET_2020[1:]])
data_2021 = Dataset([Entry(row) for row in BUDGET_2021[1:]])
data_2022 = Dataset([Entry(row) for row in BUDGET_2022[1:]])
data_2023 = Dataset([Entry(row) for row in BUDGET_2023[1:]])
data_2024 = Dataset([Entry(row) for row in BUDGET_2024[1:]])
data_2025 = Dataset([Entry(row) for row in BUDGET_2025[1:]])
data_all = Dataset([Entry(row) for row in BUDGET_ALL_YEARS[1:]])

print(f'2020   |    {data_2020.calculate_cost_estimate(1)}')
print(f'2021   |    {data_2021.calculate_cost_estimate(1)}')
print(f'2022   |    {data_2022.calculate_cost_estimate(1)}')
print(f'2023   |    {data_2023.calculate_cost_estimate(1)}')
print(f'2024   |    {data_2024.calculate_cost_estimate(1)}')
print(f'2025   |    {data_2025.calculate_cost_estimate(1)}')


print('_' * 50)

print('\nDivision Summary 2020-2025')
print(f'Division        | Cost Estimate')
print('_' * 50)

for division, estimate in data_all.division_summary().items():
    print(f'{division:<15} | {round(estimate,2)}')

print('\nKey takeaway: division 54 appeared from the dataset from 2022 and on. But this is the cost estimate for all of 2020-2025.')

# print('_' * 50)
# print('Division Summary 2020')
# print('Division       |     Cost Estimate')
# print('_' * 50)
#
# for division, estimate in data_2020.division_summary().items():
#     print(f'{division}    |     {round(estimate,2)}')
#
# print('_' * 50)
# print('Division Summary 2021')
# print('Division       |     Cost Estimate')
# print('_' * 50)
#
# for division, estimate in data_2021.division_summary().items():
#     print(f'{division}    |     {round(estimate,2)}')
#
# print('_' * 50)
# print('Division Summary 2022')
# print('Division       |     Cost Estimate')
# print('_' * 50)
#
# for division, estimate in data_2022.division_summary().items():
#     print(f'{division}    |     {round(estimate,2)}')
#
# print('_' * 50)
# print('Division Summary 2023')
# print('Division       |     Cost Estimate')
# print('_' * 50)
#
# for division, estimate in data_2023.division_summary().items():
#     print(f'{division}    |     {round(estimate,2)}')

print('_' * 50)

print('\nCategory Summary 2020-2025')
print('Category             | Cost Estimate')
print('_' * 50)

for category, estimate in data_all.category_summary().items():
    print(f'{category :<20} | {round(estimate,2)}')

