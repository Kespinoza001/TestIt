# Display welcome message
print("Welcome to the Fiber Optic Number Cruncher")

# Get the company name from the user
company_name = input(" Please enter the name of your company: ")

# Get the number of feet of fiber optic to be installed from the user
feet_requested = int(
  input("Enter the number of feet of fiber optic cable to be installed: "))

# Evaluate total cost based on the number of feet requested
if feet_requested <= 100:
  cost_per_foot = 0.87
elif feet_requested <= 250:
  cost_per_foot = 0.80
elif feet_requested <= 500:
  cost_per_foot = 0.70
else:
  cost_per_foot = 0.50

total_cost = feet_requested * cost_per_foot

# Display calculated information, including the number of feet requested and the company name
print("Company Name: ", company_name)
print("Feet Requested: ", feet_requested)
print("Cost per Foot: $", format(cost_per_foot, '.2f'))
print("Total Cost: $", format(total_cost, '.2f'))
