invested = float(input('Please enter the initial investment: '))

rate = float(input('Please enter the anual interest rate: '))

year = 0
amount = invested 

while amount  <= invested * 2 : #while loop for simple interest 

  amount = amount + amount * (rate)/100
  year = year + 1 


print('It will take: %d years to double your investment.'%(year))