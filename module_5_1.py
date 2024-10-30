class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nuber_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.nuber_of_floors:
            for i in range(new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


house = House('ЖК Эльбрус', 30)
house.go_to(5)
house.go_to(35)
