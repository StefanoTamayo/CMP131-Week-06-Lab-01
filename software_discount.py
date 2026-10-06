#Stefano Tamayo
#CMP-131
#Week 6
#Lab 1
#Software Discount Calculator
#10/6/26
unit=int(input("How many units have you purchased: "))
price=int(99)
total1=unit*price
if unit < 10:
    output="No Discount"
    discount=float("0")
elif unit >=10 and unit <= 19:
    output="Discount Percentage: 20%"
    discount=float(total1*.20)
elif unit >= 20 and unit <= 49:
    output="Discount Percentage: 30%"
    discount=float(total1*.30)
elif unit >=50 and unit <= 99:
    output="Discount Percentage: 40%"
    discount =float(total1*.40)
else:
    output="Discount Percentage: 50%"
    discount=float(total1*.5)
total2=(total1-discount)
print()
print("----------------")
if unit > 0:
    print(f"Total Units Purchased: {unit:,.2f}") 
    print(f"Price per Unit: ${price:,.2f}")
    print(f"Cost without discounts: ${total1:,.2f}")
    print(output)
    print(f"Discount Amount: ${discount:,.2f}")
    print(f"Final Purchase Cost: ${total2:,.2f}")
else:
    print("Number of units purchased must be at least 1.")