class Product:
    def __init__(self, choice, price, qnty):
        self.choice = choice
        self.price = price
        self.qnty = qnty

    #Attempted to add input options
    def from_input(self):
        choice = input("Type Product Here: ")
        price = int(input("Enter the price:$ "))
        qnty = int(input("Enter the number of items you want: "))
    

class Shopping_Cart:
    def __init__(self):
        self.product_list = []
        self.cart = []
    
    def add(self, product):
        self.product_list.append(product)

    def view(self):
        for product in self.product_list:
            print(f"{product.choice} \t {product.price} \t {product.qnty}")
    
    def add_to_cart(self, product):
        for item in self.product_list:
            if item.choice==product:
                self.cart.append(item)
                print("Item Added")
                return
        print("Item not present in store")
    
    def remove_from_cart(self, product):
        for item in self.cart:
            if item.choice==product:
                self.cart.remove(item)
                print(f"{item} deleted from cart")
                return 
        print("This product is not in your cart")
    
    def display_cart(self):
        for item in self.cart:
            print(f"{item.choice}")

sc = Shopping_Cart()
sc.add(Product("Coffee", 2, 2))
sc.add(Product("Sugar", 1, 4))
sc.add(Product("Hazelnut", 2, 1))
sc.add(Product("Cream", 1, 2))
sc.add(Product("Vanilla", 1, 8))

done=False
print("""Welcome to the Shoddy Shopping Shop.
See Products - 1
Add Product - 2
Remove Product - 3
View Cart - 4
Exit Program - 5
""")

while not done:
    selection = int(input("Enter your choice here: "))
    if selection == 1:
        sc.view()
    elif selection == 2:
       objct = input("Type product here: ")
       sc.add_to_cart(objct) 
    elif selection == 3:
        objct == input("Type the product you want removed here: ")
        sc.remove_from_cart(objct)
    elif selection == 4:
        sc.display_cart()
    elif selection == 5:
        print("The program has closed")
        break
    else:
        print("That is not a valid selection. Please enter an option 1-5")
