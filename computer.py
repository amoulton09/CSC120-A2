class Computer:
    #Attributes of computer class:

    description: str = ""
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    def __init__(self, description: str, operating_system: str, year_made: int, price: int): #Constructor that creates a computer object with all attributes listed.
        self.description = description
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def __repr__ (self): #Changes how objects of the computer class classes are represented to the resale shop when imported.
        return (f"Description: {self.description} Operating system : {self.operating_system} Year made : {self.year_made} Price : {self.price}.\n")
    
    #Methods of computer class:

    def update_price(self, price: int): #Rewrites price of computer.
        self.price = price
        return price
    
    def update_os(self, os: str): #Rewrites os of computer.
        self.operating_system = os
        return os
    
def main():
    my_computer:Computer = Computer("Black Windows Machine", "Windows 10", 2019, 450) #Creates basic computer object
    print(my_computer)
    my_computer.update_os("Windows 11") #Changes operating system
    print(my_computer)
    my_computer.update_price(400) #Changes price
    print(my_computer)

if __name__ == "__main__":
    main()