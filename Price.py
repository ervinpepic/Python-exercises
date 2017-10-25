n=input('how many items?')
min=None
max=None
for i in range(n):
    price=input ('price for the item?')
    if min is None:
        min=price;
        max=price;
    elif price<min:
        min=price
    elif price>max:
        max=price
print("the minimum is ",min)
print("the maximum is ",max)
