calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

calculate compound interest
def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t - p

 user input
p = float(input("Enter Principal amount: "))
r = float(input("Enter Interest Rate (in %): "))
t = float(input("Enter Time (in years): "))

print results
print("Simple Interest:", simple_interest(p, r, t))
print("Compound Interest:", compound_interest(p, r, t))
