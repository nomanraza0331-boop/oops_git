def delivery_charges():
    method=input("Enter delivery method as standard or prime: ")
    d=charges=0
    if method=="standard":
        d=charges=100
    elif method=="prime":
        d_charges=50
    else:
        pass 
    return d_charges
    