# Joining Multiple Sets
# Given:
rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
# The Rainfall data starts from Monday to Thursday here, if added more data,
#  it will be considered as the next day in the week.
# rainfall_chennai.append(200)
# print(rainfall_chennai)
# Print all unique rainfall measurements for Chennai and Madurai.
unique_rainfall = rainfall_chennai | rainfall_madurai
print(unique_rainfall)
# Merge all three readings into a new set using both the update() and union() methods.
new_rainfall = rainfall_chennai.union(rainfall_coimbatore,rainfall_madurai)
print(new_rainfall)
all_rainfall = rainfall_chennai
all_rainfall.update(rainfall_coimbatore,rainfall_madurai)
print(all_rainfall)
# Common Rainfall: Identify rainfall values present in all three cities.
value = rainfall_chennai & rainfall_coimbatore & rainfall_madurai
print(value)
# Unique Chennai Rainfall: Determine unique rainfall values observed exclusively in Chennai.
unique_value = rainfall_chennai - rainfall_coimbatore - rainfall_madurai
print(unique_value)
# Rainfall in at least Two Cities: Find rainfall values recorded in a minimum of two cities.
rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
min_value = min(rainfall_madurai) , min(rainfall_chennai)
print(min_value)
# Create a new set where every rainfall value is increased by 10.
increase = {x+10 for x in rainfall_chennai}
print(increase)
# For e.g. if input is {120, 140, 160,180}, then output has to be {130, 150, 170, 190}
# Delete the rainfall_coimbatore set in python.
rainfall_coimbatore = {100, 120, 180, 200}
del rainfall_coimbatore
# Clear the data inside rainfall_chennai set and make it empty.
rainfall_chennai.clear()
print(rainfall_chennai)