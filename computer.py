class Computer:
    # What attributes will it need?
    description: str = ""
    #processor_type: str = ""
    #hard_drive_capacity: int = 0
    #memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, operating_system: str, year_made: int, price: int):
        self.description = description
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        #pass # You'll remove this when you fill out your constructor

    def __repr__ (self):#Changes how classes are represented to the resale shop.
        return (f"Description: {self.description} Operating system : {self.operating_system} Year made : {self.year_made} Price : {self.price}.")
    
    # What methods will you need?
    def update_price(self, price: int): #rewrites price of computer.
        self.price = price
        return price
    
    def update_os(self, os: str): #rewrites os of computer.
        self.operating_system = os
        return os
    
def main():
    my_computer:Computer = Computer("Windows", "MyOs", 2019, 200)
    print(my_computer)
    my_computer.update_os("MyOs2")
    print(my_computer)
    my_computer.update_price(400)
    print(my_computer)

if __name__ == "__main__":
    main()