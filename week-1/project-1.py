print ("Welcome to the Financial calculator!")
print ("/n PICK A PROBLEM TO SOLVE")
print ("1.) Simple interest")
print ("2.) Compound interest")
print ("3.) Annuity plan")
decision = input("PICK A NUMBER (1-3)")

if decision == ("1"):
 p = int(input("Enter the Principal: "))
 r = int(input("Enter the Interest Rate (in %): "))
 t = int(input("Enter the Time (in years): "))
 #calculate simple interest
 simple_interest = p * (1 + ( r/100 )*t)
 print (simple_interest)

elif decision == "2":
 p = int(input("Enter the Principal: "))
 r = int(input("Enter the Interest Rate (in %): "))
 t = int(input("Enter the Time (in years): "))
 n = int(input("Enter the Compound: "))
 nt = n * t
 #calculate compound interest
 compound_interest = p * (1 + r/n)*nt
 print("Compound Interest:", compound_interest)

elif decision == "3":
 p = int(input("Enter the Principal: "))
 r = int(input("Enter the Interest Rate (in %): "))
 t = int(input("Enter the Time (in years): "))
 n = int(input("Enter the Compound: "))
 nt = n * t
 pmt = int(input("Enter the pmt: "))
 #calculate annuity plan 
 annuity_plan = pmt * ((1+r/n)*n*t - 1)/(r/n)
 print ("Annuity plan is:", annuity_plan)