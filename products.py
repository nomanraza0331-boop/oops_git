products_list=[{"pname":"kayboard","price":650,"stock_qyt":45,"category":"Electronics"},
          {"pname":"mouse","price":350,"stock_qyt":55,"category":"Electronics"},
          {"pname":"cpu","price":7500,"stock_qyt":20,"category":"Electronics"},
          {"pname":"gpu","price":11000,"stock_qyt":15,"category":"Electronics"},
          {"pname":"printer","price":10500,"stock_qyt":12,"category":"Electronics"},
          ]

def add_new_products():
    product_id=int(input("Enter product_id: "))
    products_name=input("Enter product_name: ")
    price=float(input("Enter price: "))
    stock_qyt=int(input("Enter your stock qyt: "))

products_list.append({"Product_id":product_id,
                      "product_name":product_name,
                      "price":price,
                      "stock_qyt":stock_qyt
                      }) 

def get_products_data():
    return products_list

add_new_products()
print(get_products_data())