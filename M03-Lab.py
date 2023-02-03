
#Riley Ringer
#2/2/2023
#This code is intended to gather data from the user and store said data in classes.
#Once the code is executed it will then print it out in the required format.


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# child class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # call super class
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # method to return data
    def __str__(self):
        return "Vehicle type: " + self.vehicle_type + "\nYear: " + self.year + "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: " + self.doors + "\nType of roof: " + self.roof


if __name__ == "__main__":
    # get year, make, model, doors and roof from user
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors: ")
    roof = input("Enter type of roof: ")
    # defining car
    car = Automobile("Car", year, make, model, doors, roof)
    # print details
    print(" ---- Vehicle details are ---- ")
    print(car)