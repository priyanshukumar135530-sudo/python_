
def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si


p = float(input("Enter Principal Amount: "))
t = float(input("Enter Time (in years): "))


interest = simple_interest(p, t)

print("Simple Interest:", interest)
