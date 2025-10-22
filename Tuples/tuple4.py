# Activity 4: Rainfall Data:

# The monthly_rainfall tuple provides the rainfall in millimeters for each month from January to December:

# monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)

# Calculate the total annual rainfall.
# Determine the average rainfall for the year.
# Identify the month(s) with exactly 120 mm of rainfall. (Hint: Consider using enumerate() or .count().) Print the count of months (Must have) 
# Bonus: If Possible -> Print the names of the months which had 120 mm rainfall (HINT: use a dictionary variable and map it)
# Find the highest and lowest rainfall values recorded.


# task 1

monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
total_rainfall = sum(monthly_rainfall)
print("Total annual rainfall:", total_rainfall)

# # task 2
monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
average_rainfall = total_rainfall / len(monthly_rainfall)
print("Average monthly rainfall:", average_rainfall, "mm")


# # task 3
monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
count_120 = monthly_rainfall.count(120)
print("Number of months with 120 mm rainfall:", count_120)


