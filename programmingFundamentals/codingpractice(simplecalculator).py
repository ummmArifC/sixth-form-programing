# has 3 simple calculations to go through 
# consisting of, VAT, TAX and TIME TABLE 

calculation = input('would you like to calculate vat,tax or time table:')
if calculation == 'vat':
    num1 = float(input('enter the price of the product:'))
    rate = float(input('enter the rate of vat:'))
    print(num1*rate)

if calculation == 'tax':
    income = float(input('enter your yearly income:'))
    tax_rate = float(input('enter the tax rate:'))
    new_rate = (tax_rate/100)
    print(income*new_rate)

if calculation == 'time table' or 'timetable':
    num2 = int(input('enter a number:'))
    for i in range(1,13):
        print(num2*i) 
           
else:
    print('invalid input,please try again:')
