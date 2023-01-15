total_bill = 0
name = input("Please enter your name: ")
while True:
    soft_drinks = int(input("Number of soft drinks: "))
    sandwiches = int(input("Number of sandwiches: "))

    soft_drinks_price = 17.00
    sandwich_price = 20.00

    total_bill += soft_drinks * soft_drinks_price + sandwiches * sandwich_price
    discount = total_bill * 0.15
    total_bill_less_discount = total_bill - discount

    print("\nName of customer: ", name)
    print("Total bill: ", total_bill)
    print("Discount: ", discount)
    print("Total bill less discount: ", total_bill_less_discount)
    repeat = input("\nDo you want to buy again? (yes/no): ")
    if repeat.lower() == "no":
        amount = float(input("Amount tendered: "))
        change = amount - total_bill_less_discount

        print("Change: ", change)
        break
    else:
        continue
