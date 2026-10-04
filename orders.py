import random
from products import *
from customers import *
from payment import *
from delivery import *
orders=dict()

def genrate_orders():
    order_id="ord"+str(random.randint(1,100000))
    print(order_id)
for x in get_products_data():
    print(list(x.values()))
my_products_id=int(input("Enter the product id:"))
for x in get_products_data():
    if my_products_id==list(x.values())[0]:
        print(list(x.values()))
        myqyt=int(input("Enter Qyt"))
        if myqyt>(list(x.values()))[3]:
            print("out of stock")
            break
        else:
            order_amount=myqyt*list(x.values())[2]
            print("product name:",list (x.values())[1])
            print("order Qyt:",myqyt)
            print("price:",list(x.values())[2])
            s=payment_methods
            d=delivery_charges
            print("total amount:",(order_amount+s+d))
        break
    else:
        print("product not found!")

genrate_orders


        