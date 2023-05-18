print('Welcome to Fiber Optic Cable Calculator!')
company_name = input('Please enter the name of your company:')
feet_of_cable = float(input('Please enter the number of fiber optic cable to be installed:'))
cost = feet_of_cable * 0.87
print('The total cost of installing fiber optic cable for', company_name, 'is $', cost)