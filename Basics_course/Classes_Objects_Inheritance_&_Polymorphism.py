class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self): # self is  referencing to the current instance of the class
        print("Vehicle is moving...")

    def get_make_and_model(self):
        print(f"Im a {self.make} {self.model}.")

my_car = Vehicle("Toyota", "Corolla") # creating an instance of the class

# print(my_car.make)  # accessing the attribute using the instance
# print(my_car.model) # accessing the attribute using the instance
my_car.get_make_and_model()
my_car.moves() # calling the method using the instance

your_car = Vehicle("Honda", "Civic")
your_car.get_make_and_model()
your_car.moves()


#=========================== Inheritance ========================

class Airplane(Vehicle):
    def __init__(self, make, model, idno):
        super().__init__(make, model) # calling the parent class constructor super() is used to give access to methods and properties of a parent or sibling class
        self.id = idno

    def moves(self):
        print("Airplane is flying...")

class Truck(Vehicle):
    def moves(self):
        print("Truck is driving...")

class Boat(Vehicle):
    pass

cessna = Airplane("Cessna", "172", "12345")
cessna.get_make_and_model() # inherited method
cessna.moves() # overridden method
print(cessna.id) # accessing the new attribute

ford_truck = Truck("Ford", "F-150")
ford_truck.get_make_and_model() # inherited method
ford_truck.moves() # overridden method

sailboat = Boat("Beneteau", "Oceanis")
sailboat.get_make_and_model() # inherited method    
sailboat.moves() # inherited method uses the unmodified version from Vehicle class

#=========================== Polymorphism ========================

for v in (my_car), (your_car), (cessna), (ford_truck), (sailboat):
    v.get_make_and_model() # calling the same method on different objects
    v.moves() # calling the same method on different objects
