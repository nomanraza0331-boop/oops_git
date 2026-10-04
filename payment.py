'''
x=input("enter payment methods (UPI,net_banking,COD)")
def payment_method(x):
    if x=="UPI":
        bank=input("enter your bank name")
        account_number=input("enter your account number")
        IFSC_code=input("enter your IFSC code")
        username=input("enter yout username")
    elif x=="net_banking":
        bank=input("enter your bank name: ")
        account_no=input("enter your account no")
        IFSC_code=input("enter your IFSC code")
        username=input("enter your username")
    elif x=="COD":
        address=input("enter your address")
        mobile_number=input("enter your mobile number")
    else:
        print("ERROR enter valid payment method")

payment_method()
'''
def payment_methods():
    n=input("Enter your payment method(UPI,net_banking,COD):")
    if n=="UPI" or n=="Net_banking" or n=="COD":
        if n=="COD":
            shipping_charges=100
        else:
            shipping_charges=50

    else:
        print("please select valid payment method")
        shipping_charges=0
    return shipping_charges

   


