print('WELCOME TO IZIFIN TECH')

years = float(input("Enter your number of years of experience : "))
age = float(input('Enter your age : '))

if years > 25 and age >= 55:
    print('Your Annual Tax Revenue is N5,600,000.')
elif years > 20 and age >= 45:
    print('Your Annual Tax Revenue is N4,480,000.')
elif years > 10 and age >= 35:
    print('Your Annual Tax Revenue is N1,500,000.')  
elif years < 10 and age < 35:
    print('Your Annual Tax Revenue is N550,000.')