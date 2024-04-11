class Ecommerce:
    def __init__(self):
        print("Launch Url")

    def login(self, username, password):
        print('Enter username:', username)
        print('Enter password:', password)

    def homepage(self, account, products):
        print("Account icon:", account)
        print("Products:", products)

    def basketpage(self, basketicon, addedproducts):
        print("Basket icon:", basketicon)
        print("Added Products:", addedproducts)


class Ecommerce2(Ecommerce):
    def __init__(self):
        super().__init__()
        print("Initializing Ecommerce2")

    def login(self, username, password, validation=None):
        super().login(username, password)
        print(validation)

    def homepage(self, account, products, profilevalidation=None):
        print(profilevalidation)
        super().homepage(account, products)

    def basketpage(self, basketicon, addedproducts, basketvalidation=None):
        super().basketpage(basketicon, addedproducts)
        print(basketvalidation)



if __name__ == "__main__":
    ecom2 = Ecommerce2()
    ecom2.login("Unknown", "unknown", "User successfully logged in")

    HP1 = Ecommerce2()
    HP1.homepage("Account icon visible", "Product should list", "Hello Unknown, Welcome Back")

    BP1 = Ecommerce2()
    BP1.basketpage("Basket icon should visible", "Added products should listed",
                    "List of products added successfully")
