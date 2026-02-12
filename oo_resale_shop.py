import computer
from computer import Computer #imports computer module and computer class

class ResaleShop:
    #Attributes of resale shop:

    inventory: list = []

    def __init__(self, inventory: list): #Constructor that makes a shop with an inventory.
        self.inventory = inventory

    #Methods of resale shop:

    def buy_computer(self, computer: Computer): #Adds new computer to inventory.
        self.inventory.append(computer)
        return(self.inventory)


    def sell_computer(self, computer: Computer): #Removes a computer from the inventory if it exists.
        if computer in self.inventory:
            self.inventory.remove(computer)
            return(self.inventory)
        else:
            print("No computer found!")

    def refurbish_computer(self, computer: Computer, os: str): #Change os and then price based on year made.
        if computer not in self.inventory:
            print("No computer to refurbish!!") #If no computer is in the inventory, computer is not refurbished.
        else: #Prices change based on year.
            computer.update_os(os)
            if computer.year_made >= 2020:
                computer.update_price(1000)
                return(computer)
            elif computer.year_made >= 2010:
                computer.update_price(550)
                return(computer)
            elif computer.year_made >= 2000:
                computer.update_price(0)
                return(computer)

        

def main():
    computer1:Computer = Computer("Black Windows Machine", "Windows 10", 2019, 450)
    computer2:Computer = Computer("Grey Macbook Machine", "MacOs", 2020, 1000) #Creates 2 computer objects.
    my_store:ResaleShop = ResaleShop([computer1, computer2])
    print(my_store.inventory)
    computer3 = Computer("Red Linux Machine", "Linux", 2000, 100) #Creates a 3rd computer object.
    my_store.buy_computer(computer3) 
    print(my_store.inventory)
    my_store.sell_computer(computer3)
    print(my_store.inventory) #Buys then sells computer 3, showing changed inventory.
    my_store.sell_computer(computer3) #Creates error when trying to sell computer 2 times.
    my_store.refurbish_computer(computer3, "Windows 11") #Shows error message.
    my_store.refurbish_computer(computer1, "Windows 11") #Shows new refurbished price and os.
    print(my_store.inventory)
  
if __name__ == "__main__":
    main()