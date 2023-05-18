def convert_miles_to_kilometers(miles):
   kilometers = miles * 1.609344
   
   return kilometers
   
# ask the user for input
miles = input("Enter the number of miles driven: ")
try:
   mil=int(miles)
   print(str(mil)  + " miles driven ")
   print(str(convert_miles_to_kilometers(mil)) + " kilometers driven")
except ValueError:
   print("Invalid value input")