'''Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type'''

class Flower:
    
    def __init__(self, name: str, petals: int, price: float):
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    def set_name(self, name: str):
        self._name = name

    def set_petals(self, petals: int):
        self._petals = petals

    def set_price(self, price: float):
        self._price = price

if __name__ == "__main__":
    f = Flower('Sunflower', 24, 10.50)
    print('Name of Flower:',f.get_name())
    print('No. of Petals:',f.get_petals())
    print('Price of Flower:',f.get_price())

    flowerList = []

    while input() != '':
        flowerList.append(Flower('name', -1, -1.0))
        flowerList[-1].set_name(input('Enter the name of Flower:'))
        flowerList[-1].set_petals(int(input('Number of petals:')))
        flowerList[-1].set_price(float(input('Enter Price:')))

    for i in flowerList:
        print('Name:', i.get_name())
        print('No. of Petals:', i.get_petals())
        print('Price:',i.get_price())