amount = float(input("Enter the total purchase amount:- "))
premium_member=str(input("Premium member (YES/NO):".upper()))

gen_discount=0.05
pre_discount=0.1

thresold=1000
thres_discount=0.1

if premium_member=='YES':   
    discount=pre_discount*amount
else:
    discount=gen_discount*amount

if amount>=thresold:
    total_discount=(amount*thres_discount)
else:
    total_discount=0

final_amount=amount-(discount+total_discount)

print("RECIEPT -> ")
print("Total Amount: Rs.{}".format(discount))
print("Discount Amount: Rs.{}".format(discount))
print("Thresold Discount Amount: Rs.{}".format(total_discount))
print("Billing Amount: Rs. ",final_amount)
print("Thank you for Shopping with us: ") 
