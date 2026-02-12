import computer
from computer import Computer

class ResaleShop:
    # What attributes will it need?
    inventory: list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = inventory
        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy_computer(self, computer: Computer): #adds new computer to inventory
        self.inventory.append(computer)
        return(self.inventory)

    def sell_computer(self, computer: Computer): #removes a computer from the inventory
        self.inventory.remove(computer)
        return(self.inventory)

    def refurbish_computer(self, computer: Computer, os: str): #change os and then price based on year
        if computer not in self.inventory:
            print("No Computer to refurbish!!")
        else:
            computer.update_os(os)
            if computer.year_made >= 2020:
                computer.update_price(1000)
                return(computer)
            elif computer.year_made >= 2010:
                computer.update_price(550)
                return(computer)
            elif computer.year_made >= 2000:
                computer.update_price(200)
                return(computer)

        

def main():
    computer1:Computer = Computer("Windows", "MyOs", 2014, 200)
    computer2:Computer = Computer("Mac", "MacOs", 2000, 1000)
    my_store:ResaleShop = ResaleShop([computer1, computer2])
    print(my_store.inventory)
    computer3 = Computer("Cool guy", "lala", 2000, 100)
    my_store.buy_computer(computer3)
    print(my_store.inventory)
    my_store.sell_computer(computer1)
    print(my_store.inventory)
    my_store.refurbish_computer(computer1, "My_os3")
    print(my_store.inventory)
  
if __name__ == "__main__":
    main()