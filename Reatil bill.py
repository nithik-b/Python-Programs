# To create the retail bill for the fruit's shop
# Setting the product's price
pro_list={"Apple":50.0,
         "Banana":30.0,
         "Orange":40.0,
         "Grapes":60.0,
         "Mango":100.0}
print("Welcome to the Retail Store!")
print("Product Catalog:")
#The products and it's price is calculated here.
for product,price in pro_list.items():
    print(f"{product}: {price:.1f}")
pro_name=input("Enter the product name (or 'done' to finish):")
if pro_name == "done":    
        print("Enter")

# Creating function to choose the fruit's and their quantity
def fin():
        a=int(input(f"Enter the quantity of {pro_name}:"))
        if pro_name == "Apple":
             return pro_list[pro_name]*a
        elif a == '0':
             return "Quantity must be greater than zero. Please enter a valid quantity"
        elif pro_name == "Banana":
            return pro_list[pro_name]*a
        elif pro_name == "Orange":
            return pro_list[pro_name]*a
        elif pro_name == "Grapes":
            return pro_list[pro_name]*a
        elif pro_name == "Mango":
            return pro_list[pro-name]*a
        print("Retail Bill")
# Calling the function
print(fin())    
            
