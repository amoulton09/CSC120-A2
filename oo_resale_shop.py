class ResaleShop:
    # What attributes will it need?
    inventory: list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = inventory
        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    #def buy_computer(self, item: str)


def main():
    my_store:ResaleShop = ResaleShop(["computer1", "computer2"])
    print(my_store.inventory)

if __name__ == "__main__":
    main()