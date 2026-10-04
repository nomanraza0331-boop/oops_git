# read customers data 
import random
customers_list=[{"cust_id":1001,"cust_name":"nawaz","city":"malegaon"}
                ]





def read_customers_data():
    username=input("enter your username:")
    dob=input("enter your DOB:")
    id=str(random.randint(1,100000))
    city=input("enter your city:")
    gender=input("enter your gender:")
    id=username+dob+id
    return (id,username,dob,city,gender)

    read_customers_data()