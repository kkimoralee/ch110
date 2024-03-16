# Kimora Lee
# 3-2-2024
# P2LAB1
# Assignment tests student's knowledge of how to write code that performs mathematical calculations and displays information to users

# Input
# "Enter car's gas mileage (miles/gallon): "
miles_per_gallon = float(input())
#"Enter cost of gas (dollars/gallon): "
cost_per_gallon = float(input())

# Calculate gas cost
cost_20_miles = 20 / miles_per_gallon * cost_per_gallon
cost_75_miles = 75 / miles_per_gallon * cost_per_gallon
cost_500_miles = 500 / miles_per_gallon * cost_per_gallon

# Output
print(f'{cost_20_miles:.2f} {cost_75_miles:.2f} {cost_500_miles:.2f}')
