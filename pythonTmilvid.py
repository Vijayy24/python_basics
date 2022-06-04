class superMarket:
    ''' this class about supermarket '''\

    shopName = "xys"
    marketer = "yxz"

    def __init__(self,brand,price,discount):
        self.braand = brand
        self.pricee = price
        self.discount = discount
        print("hi i'am init method")


bread = superMarket("absd",25,5)
oil = superMarket("coconut oil",180,10)
biscuits = superMarket("BoreBorn",30,3)
rice = superMarket("basmati",110,20)


print(rice.pricee)
print(superMarket.marketer)
print(superMarket.shopName)


"""
bread.brand = "xyz"
bread.price = 25

oil.brand = "coconut oil"
oil.price = 180

biscuits.brand = "BoreBorn"
biscuits.pirce = 20

rice.brand = "basmati"
rice.price = 110

print(rice.__dict__)

"""
